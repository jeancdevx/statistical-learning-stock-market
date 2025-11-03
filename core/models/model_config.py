"""
Configuración de modelos de aprendizaje estadístico.

Define los modelos a entrenar con sus hiperparámetros.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def get_models():
    """
    Retorna diccionario con configuración de modelos.
    
    Returns:
        dict: Diccionario con id, nombre y clase del modelo
    """
    modelos = {
        'logreg': {
            'nombre': 'Regresión Logística',
            'clase': lambda seed: LogisticRegression(
                max_iter=1000, 
                solver='lbfgs', 
                C=1.0, 
                random_state=seed
            )
        },
        'rf': {
            'nombre': 'Random Forest',
            'clase': lambda seed: RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                min_samples_leaf=50,
                random_state=seed,
                n_jobs=-1
            )
        },
        'svm': {
            'nombre': 'SVM-RBF',
            'clase': lambda seed: SVC(
                kernel='rbf', 
                probability=True, 
                C=1.0, 
                gamma='scale', 
                random_state=seed
            )
        }
    }
    
    return modelos
