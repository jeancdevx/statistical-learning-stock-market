from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from sklearn.preprocessing import StandardScaler


class BaseModel(ABC):
    def __init__(self, name: str, requires_scaling: bool = False):
        self.name = name
        self.requires_scaling = requires_scaling
        self.model = None
        self.scaler = None if not requires_scaling else StandardScaler()
        self.is_fitted = False
        self.feature_names = None
        
    @abstractmethod
    def _create_model(self) -> Any:
        pass
    
    def fit(self, X: pd.DataFrame, y: pd.Series) -> 'BaseModel':
        self.feature_names = X.columns.tolist()
        
        if self.requires_scaling:
            X_processed = self.scaler.fit_transform(X)
        else:
            X_processed = X.values
        
        if self.model is None:
            self.model = self._create_model()
        
        self.model.fit(X_processed, y)
        self.is_fitted = True
        
        return self
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        self._check_is_fitted()
        
        if self.requires_scaling:
            X_processed = self.scaler.transform(X)
        else:
            X_processed = X.values
        
        return self.model.predict(X_processed)
    
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        self._check_is_fitted()
        
        if self.requires_scaling:
            X_processed = self.scaler.transform(X)
        else:
            X_processed = X.values
        
        return self.model.predict_proba(X_processed)
    
    def save_model(self, path: Path) -> None:
        self._check_is_fitted()
        
        path.parent.mkdir(parents=True, exist_ok=True)
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'feature_names': self.feature_names,
            'name': self.name,
            'requires_scaling': self.requires_scaling
        }
        
        with open(path, 'wb') as f:
            pickle.dump(model_data, f)
    
    def load_model(self, path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"No se encontró el modelo en: {path}")
        
        with open(path, 'rb') as f:
            model_data = pickle.load(f)
        
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.feature_names = model_data['feature_names']
        self.name = model_data['name']
        self.requires_scaling = model_data['requires_scaling']
        self.is_fitted = True
    
    def get_hyperparameters(self) -> Dict[str, Any]:
        if self.model is None:
            self.model = self._create_model()
        
        return self.model.get_params()
    
    def _check_is_fitted(self) -> None:
        if not self.is_fitted:
            raise RuntimeError(
                f"El modelo '{self.name}' no ha sido entrenado. "
                "Llama a fit() primero."
            )
    
    def __repr__(self) -> str:
        status = "fitted" if self.is_fitted else "not fitted"
        return f"{self.__class__.__name__}(name='{self.name}', status='{status}')"
