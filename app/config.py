from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

__all__ = ['FEATURE_COLUMNS', 'DEFAULT_MODEL', 'CORS_ORIGINS']
MODELS_DIR = BASE_DIR / "models"
DATASETS_DIR = BASE_DIR / "datasets" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

DEFAULT_MODEL = "rf"

CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://nyse-predictor.vercel.app"
]

DATASET_PATH = DATASETS_DIR / "dataset_modelado.csv"

FEATURE_COLUMNS = [
    'ret_cc_1', 'ret_oo_1', 'ret_co_1',
    'sma_5', 'sma_10', 'ema_10',
    'mom_5', 'std_5', 'std_10',
    'range_rel', 'vol_ma_10', 'vol_rel', 'dow'
]
