"""
Script principal de entrenamiento de modelos.

Este es el punto de entrada para entrenar y evaluar todos los modelos
del proyecto de predicción de precios de acciones NYSE.

Uso:
    # Entrenar todos los modelos
    python train_models.py
    
    # Entrenar modelos específicos
    python train_models.py --models logreg rf
    
    # Ver ayuda
    python train_models.py --help
"""

import argparse
import sys
from pathlib import Path

# Agregar directorio raíz al path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.pipelines.training_pipeline import TrainingPipeline
from core.models.model_factory import ModelFactory
from core.config.settings import Settings


def parse_arguments():
    """Parsea argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Entrena y evalúa modelos de clasificación para predicción de precios de acciones NYSE',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Entrenar todos los modelos
  python train_models.py
  
  # Entrenar solo Regresión Logística
  python train_models.py --models logreg
  
  # Entrenar Random Forest y SVM
  python train_models.py --models rf svm
  
Modelos disponibles:
  logreg  - Regresión Logística con regularización L2
  rf      - Random Forest (ensamble de árboles)
  svm     - SVM con Stochastic Gradient Descent
        """
    )
    
    parser.add_argument(
        '--models',
        nargs='+',
        choices=ModelFactory.get_available_models(),
        help='Modelos específicos a entrenar (por defecto: todos)'
    )
    
    parser.add_argument(
        '--dataset',
        type=Path,
        default=Settings.DATASET_PATH,
        help=f'Ruta al dataset (por defecto: {Settings.DATASET_PATH})'
    )
    
    parser.add_argument(
        '--k-folds',
        type=int,
        default=Settings.K_FOLDS,
        help=f'Número de folds para walk-forward CV (por defecto: {Settings.K_FOLDS})'
    )
    
    return parser.parse_args()


def main():
    """Función principal."""
    # Parsear argumentos
    args = parse_arguments()
    
    # Banner de inicio
    print("\n" + "="*70)
    print(" "*15 + "PROYECTO: PREDICCIÓN NYSE")
    print(" "*10 + "Modelado de Dirección de Precio Overnight")
    print("="*70)
    print(f"\nConfigura ción:")
    print(f"  Dataset:     {args.dataset}")
    print(f"  K-folds:     {args.k_folds}")
    print(f"  Modelos:     {args.models or 'Todos'}")
    print(f"  Features:    {len(Settings.FEATURES)} indicadores técnicos")
    print(f"  Split:       {Settings.TRAIN_SPLIT*100:.0f}% / "
          f"{Settings.VAL_SPLIT*100:.0f}% / {Settings.TEST_SPLIT*100:.0f}%")
    print(f"  Paralelismo: {Settings.N_JOBS} cores")
    print("="*70 + "\n")
    
    # Actualizar configuración si se proporcionaron argumentos
    if args.dataset != Settings.DATASET_PATH:
        Settings.DATASET_PATH = args.dataset
    
    if args.k_folds != Settings.K_FOLDS:
        Settings.K_FOLDS = args.k_folds
    
    # Crear y ejecutar pipeline
    try:
        pipeline = TrainingPipeline(models_to_train=args.models)
        results = pipeline.run()
        
        # Verificar si hubo errores
        errors = [name for name, res in results.items() if 'error' in res]
        if errors:
            print(f"\n⚠️  ADVERTENCIA: {len(errors)} modelo(s) fallaron:")
            for model in errors:
                print(f"   - {model}: {results[model]['error']}")
            return 1
        
        print("\n✅ ENTRENAMIENTO COMPLETADO EXITOSAMENTE")
        print(f"   Resultados guardados en: {Settings.REPORTS_DIR}")
        return 0
        
    except FileNotFoundError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nAsegúrate de haber ejecutado primero:")
        print("  python core/data/make_dataset.py")
        return 1
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Entrenamiento interrumpido por el usuario")
        return 130
        
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
