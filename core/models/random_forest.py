"""
Modelo de Random Forest.

Implementación específica del modelo de ensamble basado en árboles de decisión.
"""

from sklearn.ensemble import RandomForestClassifier
from core.models.base_model import BaseModel
from core.config.settings import Settings
import numpy as np


class RandomForestModel(BaseModel):
    """
    Modelo de Random Forest para clasificación binaria.
    
    Este modelo no lineal captura interacciones complejas y umbrales que
    los modelos lineales no pueden expresar. Es robusto y no requiere
    normalización de features.
    """
    
    def __init__(self):
        """Inicializa el modelo de Random Forest."""
        config = Settings.get_model_config('rf')
        super().__init__(
            name=config['name'],
            requires_scaling=config['requires_scaling']
        )
        self.hyperparameters = config['hyperparameters']
    
    def _create_model(self) -> RandomForestClassifier:
        """
        Crea la instancia de RandomForestClassifier con hiperparámetros configurados.
        
        Returns:
            Instancia de RandomForestClassifier
        """
        return RandomForestClassifier(**self.hyperparameters)
    
    def get_feature_importance(self):
        """
        Obtiene la importancia de features basada en Gini importance.
        
        Returns:
            Diccionario ordenado por importancia descendente
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        if self.feature_names is None:
            raise RuntimeError("No hay nombres de features disponibles")
        
        # Obtener importancias del modelo
        importances = self.model.feature_importances_
        
        # Crear diccionario feature -> importancia
        feature_importance = dict(zip(self.feature_names, importances))
        
        # Ordenar por importancia descendente
        return dict(sorted(feature_importance.items(), key=lambda x: x[1], reverse=True))
    
    def get_tree_depths(self):
        """
        Obtiene las profundidades de todos los árboles en el bosque.
        
        Returns:
            Lista con la profundidad máxima de cada árbol
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        return [tree.get_depth() for tree in self.model.estimators_]
    
    def get_average_tree_depth(self):
        """
        Calcula la profundidad promedio de los árboles.
        
        Returns:
            Profundidad promedio
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        depths = self.get_tree_depths()
        return np.mean(depths)
