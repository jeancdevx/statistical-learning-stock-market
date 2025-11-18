import pickle
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class ModelLoader:
    _instance: Optional['ModelLoader'] = None
    _models: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def load_model(self, model_name: str = "rf"):
        if model_name in self._models:
            logger.info(f"Modelo {model_name} ya está en caché")
            return self._models[model_name]
        
        model_path = Path("models") / f"model_{model_name}.pkl"
        
        if not model_path.exists():
            raise FileNotFoundError(
                f"Modelo no encontrado: {model_path}\n"
                f"Modelos disponibles: {', '.join(self.get_available_models())}"
            )
        
        try:
            with open(model_path, "rb") as f:
                model_data = pickle.load(f)
            
            if isinstance(model_data, dict) and 'model' in model_data:
                model = model_data  
            else:
                model = model_data  
            
            self._models[model_name] = model
            logger.info(f"✓ Modelo {model_name} cargado exitosamente")
            return model
            
        except Exception as e:
            logger.error(f"Error cargando modelo {model_name}: {e}")
            raise RuntimeError(f"No se pudo cargar el modelo {model_name}: {str(e)}")
    
    def get_available_models(self) -> list:
        models_dir = Path("models")
        if not models_dir.exists():
            return []
        
        model_files = list(models_dir.glob("model_*.pkl"))
        return [f.stem.replace("model_", "") for f in model_files]
    
    def is_loaded(self, model_name: str) -> bool:
        return model_name in self._models
