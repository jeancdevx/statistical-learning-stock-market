from typing import List
from core.models.base_model import BaseModel
from core.models.logistic_regression import LogisticRegressionModel
from core.models.random_forest import RandomForestModel
from core.models.svm_sgd import SVMSGDModel
from core.config.settings import Settings


class ModelFactory:
    _MODELS_REGISTRY = {
        'logreg': LogisticRegressionModel,
        'rf': RandomForestModel,
        'svm': SVMSGDModel
    }
    
    @classmethod
    def create_model(cls, model_name: str) -> BaseModel:
        if model_name not in cls._MODELS_REGISTRY:
            available_models = list(cls._MODELS_REGISTRY.keys())
            raise ValueError(
                f"Modelo '{model_name}' no está registrado. "
                f"Modelos disponibles: {available_models}"
            )
        
        model_class = cls._MODELS_REGISTRY[model_name]
        return model_class()
    
    @classmethod
    def create_all_models(cls) -> List[BaseModel]:
        return [cls.create_model(name) for name in cls._MODELS_REGISTRY.keys()]
    
    @classmethod
    def get_available_models(cls) -> List[str]:
        return list(cls._MODELS_REGISTRY.keys())
    
    @classmethod
    def register_model(cls, name: str, model_class: type) -> None:
        if not issubclass(model_class, BaseModel):
            raise TypeError(
                f"La clase {model_class.__name__} debe heredar de BaseModel"
            )
        
        if name in cls._MODELS_REGISTRY:
            raise ValueError(
                f"El modelo '{name}' ya está registrado. "
                "Use un nombre diferente o elimine el existente primero."
            )
        
        cls._MODELS_REGISTRY[name] = model_class
    
    @classmethod
    def unregister_model(cls, name: str) -> None:
        if name not in cls._MODELS_REGISTRY:
            raise ValueError(f"Modelo '{name}' no está registrado")
        
        del cls._MODELS_REGISTRY[name]
