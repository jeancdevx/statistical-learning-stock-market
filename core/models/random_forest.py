from sklearn.ensemble import RandomForestClassifier
from core.models.base_model import BaseModel
from core.config.settings import Settings
import numpy as np


class RandomForestModel(BaseModel):
    def __init__(self):
        config = Settings.get_model_config('rf')
        super().__init__(
            name=config['name'],
            requires_scaling=config['requires_scaling']
        )
        self.hyperparameters = config['hyperparameters']
    
    def _create_model(self) -> RandomForestClassifier:
        return RandomForestClassifier(**self.hyperparameters)
    
    def get_feature_importance(self):
        self._check_is_fitted()
        
        if self.feature_names is None:
            raise RuntimeError("No hay nombres de features disponibles")
        
        importances = self.model.feature_importances_
        
        feature_importance = dict(zip(self.feature_names, importances))
        
        return dict(sorted(feature_importance.items(), key=lambda x: x[1], reverse=True))
    
    def get_tree_depths(self):
        self._check_is_fitted()
        
        return [tree.get_depth() for tree in self.model.estimators_]
    
    def get_average_tree_depth(self):
        depths = self.get_tree_depths()
        return np.mean(depths)
