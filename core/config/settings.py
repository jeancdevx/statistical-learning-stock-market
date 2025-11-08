"""
Configuración centralizada del proyecto.

Este módulo contiene todas las configuraciones y constantes utilizadas
en el proyecto de predicción de precios de acciones NYSE.
"""

import os
from pathlib import Path


class Settings:
    """Configuración centralizada del proyecto."""
    
    # ==================== RUTAS ====================
    # Directorio raíz del proyecto
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    
    # Rutas de datos
    DATA_DIR = PROJECT_ROOT / "datasets"
    RAW_DATA_DIR = DATA_DIR / "nyse" / "data" / "daily" / "us"
    PROCESSED_DATA_DIR = DATA_DIR / "processed"
    DATASET_PATH = PROCESSED_DATA_DIR / "dataset_modelado.csv"
    
    # Rutas de salida
    REPORTS_DIR = PROJECT_ROOT / "reports"
    METRICS_DIR = REPORTS_DIR / "metrics"
    FIGURES_DIR = REPORTS_DIR / "figures"
    MODELS_DIR = PROJECT_ROOT / "models"
    
    # ==================== DIVISIÓN TEMPORAL ====================
    TRAIN_SPLIT = 0.75  # 75% para entrenamiento
    VAL_SPLIT = 0.10    # 10% para validación
    TEST_SPLIT = 0.15   # 15% para prueba
    
    # Validación cruzada
    K_FOLDS = 5  # Número de folds para walk-forward CV
    
    # ==================== PREPROCESAMIENTO ====================
    # Ventana de warm-up para indicadores técnicos
    WARM_UP_WINDOW = 10
    
    # Características a utilizar
    FEATURES = [
        'ret_cc_1',   # Retorno close-to-close
        'ret_oo_1',   # Retorno open-to-open
        'ret_co_1',   # Retorno close-to-open (gap overnight)
        'sma_5',      # Media móvil simple 5 días
        'sma_10',     # Media móvil simple 10 días
        'ema_10',     # Media móvil exponencial 10 días
        'mom_5',      # Momentum 5 días
        'std_5',      # Volatilidad 5 días
        'std_10',     # Volatilidad 10 días
        'range_rel',  # Rango relativo intradía
        'vol_ma_10',  # Media móvil del volumen
        'vol_rel',    # Volumen relativo
        'dow'         # Día de la semana
    ]
    
    TARGET = 'target'  # Variable objetivo (dirección overnight)
    
    # ==================== MODELOS ====================
    # Semilla para reproducibilidad
    RANDOM_STATE = 42
    
    # Paralelización (ajustar según tu hardware)
    N_JOBS = 8  # Número de núcleos a utilizar
    
    # Configuración de modelos
    MODELS_CONFIG = {
        'logreg': {
            'name': 'Logistic Regression',
            'short_name': 'logreg',
            'requires_scaling': True,
            'hyperparameters': {
                'penalty': 'l2',
                'C': 1.0,
                'solver': 'lbfgs',
                'max_iter': 1000,
                'random_state': RANDOM_STATE,
                'n_jobs': N_JOBS
            }
        },
        'rf': {
            'name': 'Random Forest',
            'short_name': 'rf',
            'requires_scaling': False,
            'hyperparameters': {
                'n_estimators': 100,
                'max_depth': 10,
                'min_samples_split': 2,
                'min_samples_leaf': 1,
                'random_state': RANDOM_STATE,
                'n_jobs': N_JOBS
            }
        },
        'svm': {
            'name': 'SVM-SGD',
            'short_name': 'svm',
            'requires_scaling': True,
            'hyperparameters': {
                'loss': 'log_loss',  # Para permitir predict_proba
                'penalty': 'l2',
                'alpha': 0.0001,
                'max_iter': 2000,
                'tol': 1e-3,
                'random_state': RANDOM_STATE,
                'n_jobs': N_JOBS
            }
        }
    }
    
    # ==================== MÉTRICAS ====================
    # Métricas principales a calcular
    METRICS = [
        'accuracy',
        'balanced_accuracy',
        'precision',
        'recall',
        'f1',
        'roc_auc'
    ]
    
    # ==================== VISUALIZACIÓN ====================
    FIGURE_DPI = 300
    FIGURE_SIZE = (10, 8)
    
    # ==================== LOGGING ====================
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    @classmethod
    def create_directories(cls):
        """Crea todos los directorios necesarios si no existen."""
        directories = [
            cls.PROCESSED_DATA_DIR,
            cls.METRICS_DIR,
            cls.FIGURES_DIR,
            cls.MODELS_DIR
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_model_config(cls, model_name: str) -> dict:
        """
        Obtiene la configuración de un modelo específico.
        
        Args:
            model_name: Nombre corto del modelo ('logreg', 'rf', 'svm')
            
        Returns:
            Diccionario con la configuración del modelo
            
        Raises:
            ValueError: Si el modelo no existe en la configuración
        """
        if model_name not in cls.MODELS_CONFIG:
            raise ValueError(
                f"Modelo '{model_name}' no encontrado. "
                f"Modelos disponibles: {list(cls.MODELS_CONFIG.keys())}"
            )
        return cls.MODELS_CONFIG[model_name]
    
    @classmethod
    def get_output_paths(cls, model_short_name: str) -> dict:
        """
        Genera las rutas de salida para un modelo específico.
        
        Args:
            model_short_name: Nombre corto del modelo
            
        Returns:
            Diccionario con rutas de métricas, modelo y figuras
        """
        return {
            'val_metrics': cls.METRICS_DIR / f"val_cv_summary_{model_short_name}.csv",
            'test_metrics': cls.METRICS_DIR / f"test_metrics_{model_short_name}.json",
            'confusion_matrix': cls.FIGURES_DIR / f"confusion_matrix_{model_short_name}.png",
            'model_file': cls.MODELS_DIR / f"model_{model_short_name}.pkl"
        }
