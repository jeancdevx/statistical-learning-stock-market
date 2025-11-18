import pandas as pd
import json
from pathlib import Path
from typing import List, Optional
import logging

from core.config.settings import Settings
from core.models.model_factory import ModelFactory
from core.models.validation import validacion_walk_forward
from core.models.evaluate import evaluar_en_test
from core.utils.visualization import guardar_matriz_confusion


logging.basicConfig(
    level=Settings.LOG_LEVEL,
    format=Settings.LOG_FORMAT
)
logger = logging.getLogger(__name__)


class TrainingPipeline:
    def __init__(self, models_to_train: Optional[List[str]] = None):
        self.models_to_train = models_to_train or ModelFactory.get_available_models()
        self.results = {}
        
        Settings.create_directories()
        
        logger.info(f"Pipeline inicializado con modelos: {self.models_to_train}")
    
    def load_data(self) -> tuple:
        logger.info(f"Cargando dataset desde: {Settings.DATASET_PATH}")
        
        if not Settings.DATASET_PATH.exists():
            raise FileNotFoundError(
                f"Dataset no encontrado en: {Settings.DATASET_PATH}\n"
            )
        
        df = pd.read_csv(Settings.DATASET_PATH, parse_dates=['Date'])
        logger.info(f"Dataset cargado: {len(df):,} registros, {len(df['Ticker'].unique())} tickers")
        
        df = df.sort_values(['Ticker', 'Date']).reset_index(drop=True)
        
        n = len(df)
        train_end = int(n * Settings.TRAIN_SPLIT)
        val_end = int(n * (Settings.TRAIN_SPLIT + Settings.VAL_SPLIT))
        
        train_df = df.iloc[:train_end].copy()
        val_df = df.iloc[train_end:val_end].copy()
        test_df = df.iloc[val_end:].copy()
        train_val_df = df.iloc[:val_end].copy()
        
        logger.info(f"División temporal completada:")
        logger.info(f"  Train: {len(train_df):,} ({Settings.TRAIN_SPLIT*100:.0f}%)")
        logger.info(f"  Val:   {len(val_df):,} ({Settings.VAL_SPLIT*100:.0f}%)")
        logger.info(f"  Test:  {len(test_df):,} ({Settings.TEST_SPLIT*100:.0f}%)")
        
        return train_df, val_df, test_df, train_val_df
    
    def train_and_evaluate_model(
        self,
        model_name: str,
        train_df: pd.DataFrame,
        val_df: pd.DataFrame,
        test_df: pd.DataFrame,
        train_val_df: pd.DataFrame
    ) -> dict:
        logger.info(f"\n{'='*70}")
        logger.info(f"INICIANDO: {model_name.upper()}")
        logger.info(f"{'='*70}")
        
        model = ModelFactory.create_model(model_name)
        
        output_paths = Settings.get_output_paths(model_name)
        
        logger.info(f"\nFase 1: Validación Walk-Forward (k={Settings.K_FOLDS})")
        metricas_folds, metricas_promedio = validacion_walk_forward(
            model=model,
            train_df=train_df,
            val_df=val_df,
            features=Settings.FEATURES,
            k=Settings.K_FOLDS
        )
        
        val_df_metrics = pd.DataFrame(metricas_folds)
        val_df_metrics.to_csv(output_paths['val_metrics'], index=False)
        logger.info(f"  ✓ Métricas de validación guardadas en: {output_paths['val_metrics']}")
        
        logger.info(f"\nFase 2: Evaluación en Test")
        metricas_test, cm = evaluar_en_test(
            model=model,
            train_val_df=train_val_df,
            test_df=test_df,
            features=Settings.FEATURES
        )
        
        with open(output_paths['test_metrics'], 'w') as f:
            json.dump(metricas_test, f, indent=2)
        logger.info(f"  ✓ Métricas de test guardadas en: {output_paths['test_metrics']}")
        
        logger.info(f"\nFase 3: Generación de Visualizaciones")
        guardar_matriz_confusion(
            cm=cm,
            nombre_modelo=model.name,
            ruta=output_paths['confusion_matrix']
        )
        logger.info(f"  ✓ Matriz de confusión guardada en: {output_paths['confusion_matrix']}")
        
        model.save_model(output_paths['model_file'])
        logger.info(f"  ✓ Modelo guardado en: {output_paths['model_file']}")
        
        results = {
            'model_name': model.name,
            'model_short_name': model_name,
            'validation': {
                'folds': metricas_folds,
                'summary': metricas_promedio
            },
            'test': metricas_test,
            'output_paths': {k: str(v) for k, v in output_paths.items()}
        }
        
        logger.info(f"\n{'='*70}")
        logger.info(f"COMPLETADO: {model_name.upper()}")
        logger.info(f"  ROC-AUC (Val):  {metricas_promedio['roc_auc_mean']:.4f} ± "
                   f"{metricas_promedio['roc_auc_std']:.4f}")
        logger.info(f"  ROC-AUC (Test): {metricas_test['roc_auc']:.4f}")
        logger.info(f"{'='*70}\n")
        
        return results
    
    def run(self) -> dict:
        logger.info("\n" + "="*70)
        logger.info("PIPELINE DE ENTRENAMIENTO INICIADO")
        logger.info("="*70)
        
        train_df, val_df, test_df, train_val_df = self.load_data()
        
        for model_name in self.models_to_train:
            try:
                results = self.train_and_evaluate_model(
                    model_name=model_name,
                    train_df=train_df,
                    val_df=val_df,
                    test_df=test_df,
                    train_val_df=train_val_df
                )
                self.results[model_name] = results
                
            except Exception as e:
                logger.error(f"Error al entrenar {model_name}: {str(e)}", exc_info=True)
                self.results[model_name] = {'error': str(e)}
        
        self._print_final_summary()
        
        return self.results
    
    def _print_final_summary(self):
        logger.info("\n" + "="*70)
        logger.info("RESUMEN FINAL - COMPARACIÓN DE MODELOS")
        logger.info("="*70)
        
        comparison = []
        for model_name, results in self.results.items():
            if 'error' not in results:
                comparison.append({
                    'Modelo': results['model_name'],
                    'Accuracy': results['test']['accuracy'],
                    'Balanced Acc': results['test']['balanced_accuracy'],
                    'F1-Score': results['test']['f1'],
                    'ROC-AUC': results['test']['roc_auc']
                })
        
        if comparison:
            df_comparison = pd.DataFrame(comparison)
            df_comparison = df_comparison.sort_values('ROC-AUC', ascending=False)
            
            logger.info("\nMétricas en conjunto de test (ordenado por ROC-AUC):")
            logger.info("")
            logger.info(df_comparison.to_string(index=False, float_format='%.4f'))
            
            best_model = df_comparison.iloc[0]
            logger.info(f"\n🏆 MEJOR MODELO: {best_model['Modelo']}")
            logger.info(f"   ROC-AUC: {best_model['ROC-AUC']:.4f}")
            logger.info(f"   Accuracy: {best_model['Accuracy']:.4f}")
            
            comparison_path = Settings.METRICS_DIR / "models_comparison.csv"
            df_comparison.to_csv(comparison_path, index=False)
            logger.info(f"\n✓ Comparación guardada en: {comparison_path}")
        
        logger.info("\n" + "="*70)
        logger.info("PIPELINE COMPLETADO EXITOSAMENTE")
        logger.info("="*70 + "\n")
