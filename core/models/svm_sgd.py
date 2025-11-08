"""
Modelo SVM con Stochastic Gradient Descent.

Implementación específica de SVM lineal optimizado para grandes datasets.
"""

from sklearn.linear_model import SGDClassifier
from core.models.base_model import BaseModel
from core.config.settings import Settings


class SVMSGDModel(BaseModel):
    """
    Modelo SVM con entrenamiento SGD para clasificación binaria.
    
    Este modelo es eficiente para datasets grandes y puede capturar
    relaciones no lineales cuando se usan kernels apropiados.
    Usa loss='log_loss' para permitir estimación de probabilidades.
    """
    
    def __init__(self):
        """Inicializa el modelo SVM-SGD."""
        config = Settings.get_model_config('svm')
        super().__init__(
            name=config['name'],
            requires_scaling=config['requires_scaling']
        )
        self.hyperparameters = config['hyperparameters']
    
    def _create_model(self) -> SGDClassifier:
        """
        Crea la instancia de SGDClassifier con hiperparámetros configurados.
        
        Returns:
            Instancia de SGDClassifier
        """
        return SGDClassifier(**self.hyperparameters)
    
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
        
        Para modelos lineales como SVM, la importancia se calcula como
        el valor absoluto de los coeficientes.
        
        Returns:
            Diccionario ordenado por importancia descendente
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        coeffs = self.get_coefficients()
        # Ordenar por valor absoluto (importancia)
        return dict(sorted(coeffs.items(), key=lambda x: abs(x[1]), reverse=True))
    
    def get_iterations_run(self):
        """
        Obtiene el número de iteraciones realizadas durante el entrenamiento.
        
        Returns:
            Número de iteraciones
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        return self.model.n_iter_
