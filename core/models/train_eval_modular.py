import pandas as pd
import json
from pathlib import Path
import warnings
import sys
warnings.filterwarnings('ignore')

# Importar módulos propios
from model_config import get_models
from validation import validacion_walk_forward
from evaluate import evaluar_en_test
sys.path.append(str(Path(__file__).parent.parent))
from utils.visualization import guardar_matriz_confusion


def main():
    print("="*60)
    print("PASO 3: Entrenamiento y Evaluación (5.1)")
    print("="*60)
    print()
    
    # Cargar dataset
    dataset_path = Path("datasets/processed/dataset_modelado.csv")
    
    if not dataset_path.exists():
        print(f"✗ Error: No se encuentra {dataset_path}")
        print("  Ejecuta primero: python core/data/make_dataset.py")
        return
    
    print(f"Cargando dataset desde: {dataset_path}")
    print("(Esto puede tomar 1-2 minutos con 10M de registros...)")
    
    # Carga optimizada con tipos de datos especificados
    df = pd.read_csv(
        dataset_path, 
        parse_dates=['Date'],
        dtype={
            'Ticker': 'category',      # Ahorra memoria
            'split': 'category',        # Ahorra memoria
            'dow': 'int8',              # 0-4 cabe en int8
            'target': 'int8'            # 0-1 cabe en int8
        }
    )
    
    print(f"✓ Dataset cargado: {len(df):,} registros")
    print()
    
    # Separar conjuntos
    train_df = df[df['split'] == 'train'].copy()
    val_df = df[df['split'] == 'val'].copy()
    test_df = df[df['split'] == 'test'].copy()
    train_val_df = pd.concat([train_df, val_df], ignore_index=True)
    
    print(f"Distribución:")
    print(f"  Train: {len(train_df):,} ({len(train_df)/len(df)*100:.1f}%)")
    print(f"  Val:   {len(val_df):,} ({len(val_df)/len(df)*100:.1f}%)")
    print(f"  Test:  {len(test_df):,} ({len(test_df)/len(df)*100:.1f}%)")
    print()
    
    # Features
    features = ['ret_cc_1', 'ret_oo_1', 'ret_co_1', 'sma_5', 'sma_10', 
                'ema_10', 'mom_5', 'std_5', 'std_10', 'range_rel', 
                'vol_ma_10', 'vol_rel', 'dow']
    
    print(f"Features: {len(features)}")
    print(f"  {', '.join(features[:6])},")
    print(f"  {', '.join(features[6:])}")
    print()
    
    # Crear directorios de salida
    Path("reports/metrics").mkdir(parents=True, exist_ok=True)
    Path("reports/figures").mkdir(parents=True, exist_ok=True)
    
    # Obtener modelos
    modelos = get_models()
    seed = 42
    k_folds = 5  # Validación robusta con 5 folds (máxima precisión)
    
    # Entrenar y evaluar cada modelo
    for modelo_id, modelo_info in modelos.items():
        nombre = modelo_info['nombre']
        modelo_class = modelo_info['clase']
        
        print(f"\n{'#'*60}")
        print(f"# MODELO: {nombre}")
        print(f"{'#'*60}")
        
        # Validación walk-forward
        metricas_folds, resumen_val = validacion_walk_forward(
            train_df, val_df, features, modelo_class, nombre, k=k_folds, seed=seed
        )
        
        # Guardar resumen de validación
        df_folds = pd.DataFrame(metricas_folds)
        df_folds.to_csv(f"reports/metrics/val_cv_summary_{modelo_id}.csv", index=False)
        print(f"  ✓ Guardado: reports/metrics/val_cv_summary_{modelo_id}.csv")
        
        # Evaluación en test
        metricas_test, cm = evaluar_en_test(
            train_val_df, test_df, features, modelo_class, nombre, seed=seed
        )
        
        # Guardar métricas de test
        metricas_test['validacion'] = resumen_val
        with open(f"reports/metrics/test_metrics_{modelo_id}.json", 'w') as f:
            json.dump(metricas_test, f, indent=2)
        print(f"  ✓ Guardado: reports/metrics/test_metrics_{modelo_id}.json")
        
        # Guardar matriz de confusión
        guardar_matriz_confusion(cm, nombre, "reports/figures")
    
    # Resumen final
    print(f"\n{'='*60}")
    print("RESUMEN FINAL")
    print(f"{'='*60}")
    print()
    print("Archivos generados:")
    print("  reports/metrics/")
    print("    - test_metrics_logreg.json")
    print("    - test_metrics_rf.json")
    print("    - test_metrics_svm.json")
    print("    - val_cv_summary_logreg.csv")
    print("    - val_cv_summary_rf.csv")
    print("    - val_cv_summary_svm.csv")
    print("  reports/figures/")
    print("    - confusion_matrix_regresión_logística.png")
    print("    - confusion_matrix_random_forest.png")
    print("    - confusion_matrix_svm-rbf.png")
    print()
    print("="*60)
    print("✓ PASO 3 COMPLETADO")
    print("="*60)


if __name__ == "__main__":
    main()
