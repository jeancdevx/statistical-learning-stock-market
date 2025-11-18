import os
from pathlib import Path


class Settings:
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    
    DATA_DIR = PROJECT_ROOT / "datasets"
    RAW_DATA_DIR = DATA_DIR / "nyse" / "data" / "daily" / "us"
    PROCESSED_DATA_DIR = DATA_DIR / "processed"
    DATASET_PATH = PROCESSED_DATA_DIR / "dataset_modelado.csv"
    
    REPORTS_DIR = PROJECT_ROOT / "reports"
    METRICS_DIR = REPORTS_DIR / "metrics"
    FIGURES_DIR = REPORTS_DIR / "figures"
    MODELS_DIR = PROJECT_ROOT / "models"
    
    TRAIN_SPLIT = 0.75  
    VAL_SPLIT = 0.10    
    TEST_SPLIT = 0.15   
    
    K_FOLDS = 5
    
    WARM_UP_WINDOW = 10
    
    FEATURES = [
        'ret_cc_1',   
        'ret_oo_1',   
        'ret_co_1',   
        'sma_5',      
        'sma_10',     
        'ema_10',     
        'mom_5',      
        'std_5',      
        'std_10',     
        'range_rel',  
        'vol_ma_10',  
        'vol_rel',    
        'dow'        
    ]
    
    TARGET = 'target'  
    
    RANDOM_STATE = 42
    
    N_JOBS = 8
    
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
                'loss': 'log_loss',  
                'penalty': 'l2',
                'alpha': 0.0001,
                'max_iter': 2000,
                'tol': 1e-3,
                'random_state': RANDOM_STATE,
                'n_jobs': N_JOBS
            }
        }
    }
    
    METRICS = [
        'accuracy',
        'balanced_accuracy',
        'precision',
        'recall',
        'f1',
        'roc_auc'
    ]
    
    FIGURE_DPI = 300
    FIGURE_SIZE = (10, 8)
    
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    @classmethod
    def create_directories(cls):
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
        if model_name not in cls.MODELS_CONFIG:
            raise ValueError(
                f"Modelo '{model_name}' no encontrado. "
                f"Modelos disponibles: {list(cls.MODELS_CONFIG.keys())}"
            )
        return cls.MODELS_CONFIG[model_name]
    
    @classmethod
    def get_output_paths(cls, model_short_name: str) -> dict:
        return {
            'val_metrics': cls.METRICS_DIR / f"val_cv_summary_{model_short_name}.csv",
            'test_metrics': cls.METRICS_DIR / f"test_metrics_{model_short_name}.json",
            'confusion_matrix': cls.FIGURES_DIR / f"confusion_matrix_{model_short_name}.png",
            'model_file': cls.MODELS_DIR / f"model_{model_short_name}.pkl"
        }
