"""
Modelo de Regresión Logística.

Implementación específica del modelo lineal con regularización L2.
"""

from sklearn.linear_model import LogisticRegression
from core.models.base_model import BaseModel
from core.config.settings import Settings


class LogisticRegressionModel(BaseModel):
    """
    Modelo de Regresión Logística con regularización L2.
    
    Este modelo sirve como línea base interpretable para clasificación binaria.
    Permite cuantificar el efecto marginal de las señales técnicas sobre
    la probabilidad de alza en la apertura.
    """
    
    def __init__(self):
        """Inicializa el modelo de Regresión Logística."""
        config = Settings.get_model_config('logreg')
        super().__init__(
            name=config['name'],
            requires_scaling=config['requires_scaling']
        )
        self.hyperparameters = config['hyperparameters']
    
    def _create_model(self) -> LogisticRegression:
        """
        Crea la instancia de LogisticRegression con hiperparámetros configurados.
        
        Returns:
            Instancia de LogisticRegression
        """
        return LogisticRegression(**self.hyperparameters)
    
    def get_coefficients(self):
        """
        Obtiene los coeficientes del modelo entrenado.
        
        Returns:
            Diccionario con feature names y sus coeficientes
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        if self.feature_names is None:
            raise RuntimeError("No hay nombres de features disponibles")
        
        return dict(zip(self.feature_names, self.model.coef_[0]))
    
    def get_feature_importance(self):
        """
        Obtiene la importancia de features (valor absoluto de coeficientes).
        
        Returns:
            Diccionario ordenado por importancia descendente
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        coeffs = self.get_coefficients()
        # Ordenar por valor absoluto (importancia)
        return dict(sorted(coeffs.items(), key=lambda x: abs(x[1]), reverse=True))
