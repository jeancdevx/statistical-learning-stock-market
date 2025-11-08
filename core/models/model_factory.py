"""
Factory para creación de modelos.

Implementa el patrón Factory para instanciar modelos de forma dinámica.
"""

from typing import List
from core.models.base_model import BaseModel
from core.models.logistic_regression import LogisticRegressionModel
from core.models.random_forest import RandomForestModel
from core.models.svm_sgd import SVMSGDModel
from core.config.settings import Settings


class ModelFactory:
    """
    Factory para crear instancias de modelos.
    
    Permite crear modelos de forma dinámica sin acoplamiento fuerte
    entre el código cliente y las clases concretas de modelos.
    """
    
    # Registro de modelos disponibles
    _MODELS_REGISTRY = {
        'logreg': LogisticRegressionModel,
        'rf': RandomForestModel,
        'svm': SVMSGDModel
    }
    
    @classmethod
    def create_model(cls, model_name: str) -> BaseModel:
        """
        Crea una instancia de un modelo específico.
        
        Args:
            model_name: Nombre corto del modelo ('logreg', 'rf', 'svm')
            
        Returns:
            Instancia del modelo solicitado
            
        Raises:
            ValueError: Si el modelo no está registrado
            
        Example:
            >>> factory = ModelFactory()
            >>> model = factory.create_model('logreg')
            >>> print(model.name)
            'Logistic Regression'
        """
        if model_name not in cls._MODELS_REGISTRY:
            available_models = list(cls._MODELS_REGISTRY.keys())
            raise ValueError(
                f"Modelo '{model_name}' no está registrado. "
                f"Modelos disponibles: {available_models}"
            )
        
        # Obtener la clase del modelo y crear instancia
        model_class = cls._MODELS_REGISTRY[model_name]
        return model_class()
    
    @classmethod
    def create_all_models(cls) -> List[BaseModel]:
        """
        Crea instancias de todos los modelos registrados.
        
        Returns:
            Lista con instancias de todos los modelos
            
        Example:
            >>> factory = ModelFactory()
            >>> models = factory.create_all_models()
            >>> print([m.name for m in models])
            ['Logistic Regression', 'Random Forest', 'SVM-SGD']
        """
        return [cls.create_model(name) for name in cls._MODELS_REGISTRY.keys()]
    
    @classmethod
    def get_available_models(cls) -> List[str]:
        """
        Obtiene la lista de modelos disponibles.
        
        Returns:
            Lista con nombres cortos de modelos disponibles
        """
        return list(cls._MODELS_REGISTRY.keys())
    
    @classmethod
    def register_model(cls, name: str, model_class: type) -> None:
        """
        Registra un nuevo modelo en el factory.
        
        Permite extender el factory con nuevos modelos sin modificar código existente
        (Principio Open/Closed de SOLID).
        
        Args:
            name: Nombre corto del modelo
            model_class: Clase del modelo (debe heredar de BaseModel)
            
        Raises:
            TypeError: Si la clase no hereda de BaseModel
            ValueError: Si el nombre ya está registrado
            
        Example:
            >>> from core.models.base_model import BaseModel
            >>> class NewModel(BaseModel):
            ...     pass
            >>> ModelFactory.register_model('new_model', NewModel)
        """
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
        """
        Elimina un modelo del registro.
        
        Args:
            name: Nombre corto del modelo a eliminar
            
        Raises:
            ValueError: Si el modelo no está registrado
        """
        if name not in cls._MODELS_REGISTRY:
            raise ValueError(f"Modelo '{name}' no está registrado")
        
        del cls._MODELS_REGISTRY[name]
