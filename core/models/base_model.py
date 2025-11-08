"""
Clase abstracta base para todos los modelos de clasificación.

Este módulo define la interfaz común que deben implementar todos los modelos,
siguiendo el principio de Open/Closed (SOLID).
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from sklearn.preprocessing import StandardScaler


class BaseModel(ABC):
    """
    Clase abstracta base para modelos de clasificación binaria.
    
    Todos los modelos específicos (LogReg, RF, SVM) deben heredar de esta clase
    e implementar los métodos abstractos.
    """
    
    def __init__(self, name: str, requires_scaling: bool = False):
        """
        Inicializa el modelo base.
        
        Args:
            name: Nombre descriptivo del modelo
            requires_scaling: Si el modelo requiere normalización de features
        """
        self.name = name
        self.requires_scaling = requires_scaling
        self.model = None
        self.scaler = None if not requires_scaling else StandardScaler()
        self.is_fitted = False
        self.feature_names = None
        
    @abstractmethod
    def _create_model(self) -> Any:
        """
        Crea la instancia del modelo de scikit-learn.
        
        Returns:
            Instancia del modelo (ej: LogisticRegression, RandomForestClassifier)
        """
        pass
    
    def fit(self, X: pd.DataFrame, y: pd.Series) -> 'BaseModel':
        """
        Entrena el modelo con los datos proporcionados.
        
        Args:
            X: DataFrame con features
            y: Serie con target (0 o 1)
            
        Returns:
            self (para permitir method chaining)
        """
        # Guardar nombres de features
        self.feature_names = X.columns.tolist()
        
        # Aplicar scaling si es necesario
        if self.requires_scaling:
            X_processed = self.scaler.fit_transform(X)
        else:
            X_processed = X.values
        
        # Crear modelo si no existe
        if self.model is None:
            self.model = self._create_model()
        
        # Entrenar
        self.model.fit(X_processed, y)
        self.is_fitted = True
        
        return self
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Realiza predicciones de clase (0 o 1).
        
        Args:
            X: DataFrame con features
            
        Returns:
            Array con predicciones (0 o 1)
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        # Aplicar scaling si es necesario
        if self.requires_scaling:
            X_processed = self.scaler.transform(X)
        else:
            X_processed = X.values
        
        return self.model.predict(X_processed)
    
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Calcula probabilidades de pertenencia a cada clase.
        
        Args:
            X: DataFrame con features
            
        Returns:
            Array de shape (n_samples, 2) con probabilidades
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        # Aplicar scaling si es necesario
        if self.requires_scaling:
            X_processed = self.scaler.transform(X)
        else:
            X_processed = X.values
        
        return self.model.predict_proba(X_processed)
    
    def save_model(self, path: Path) -> None:
        """
        Guarda el modelo entrenado en disco.
        
        Args:
            path: Ruta donde guardar el modelo
            
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        self._check_is_fitted()
        
        # Crear directorio si no existe
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Guardar modelo completo (incluyendo scaler)
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
        """
        Carga un modelo previamente guardado.
        
        Args:
            path: Ruta del modelo guardado
            
        Raises:
            FileNotFoundError: Si el archivo no existe
        """
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
        """
        Obtiene los hiperparámetros del modelo.
        
        Returns:
            Diccionario con hiperparámetros
            
        Raises:
            RuntimeError: Si el modelo no ha sido creado
        """
        if self.model is None:
            self.model = self._create_model()
        
        return self.model.get_params()
    
    def _check_is_fitted(self) -> None:
        """
        Verifica que el modelo haya sido entrenado.
        
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado
        """
        if not self.is_fitted:
            raise RuntimeError(
                f"El modelo '{self.name}' no ha sido entrenado. "
                "Llama a fit() primero."
            )
    
    def __repr__(self) -> str:
        """Representación en string del modelo."""
        status = "fitted" if self.is_fitted else "not fitted"
        return f"{self.__class__.__name__}(name='{self.name}', status='{status}')"
