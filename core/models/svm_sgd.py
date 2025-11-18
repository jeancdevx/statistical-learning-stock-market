from sklearn.linear_model import SGDClassifier
from core.models.base_model import BaseModel
from core.config.settings import Settings


class SVMSGDModel(BaseModel):
    def __init__(self):
        config = Settings.get_model_config('svm')
        super().__init__(
            name=config['name'],
            requires_scaling=config['requires_scaling']
        )
        self.hyperparameters = config['hyperparameters']
    
    def _create_model(self) -> SGDClassifier:
        return SGDClassifier(**self.hyperparameters)
    
    def get_coefficients(self):
        self._check_is_fitted()
        
        if self.feature_names is None:
            raise RuntimeError("No hay nombres de features disponibles")
        
        return dict(zip(self.feature_names, self.model.coef_[0]))
    
    def get_feature_importance(self):
        coeffs = self.get_coefficients()
        return dict(sorted(coeffs.items(), key=lambda x: abs(x[1]), reverse=True))
    
    def get_iterations_run(self):
        self._check_is_fitted()
        
        return self.model.n_iter_
