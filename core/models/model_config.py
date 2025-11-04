"""
Configuración de modelos de aprendizaje estadístico.

Define los modelos a entrenar con sus hiperparámetros.
OPTIMIZADO para hardware: 16GB RAM, 8 núcleos - 10M registros.
"""

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier


def get_models():
    """
    Configura 3 modelos con máxima precisión:
    - LogReg: Baseline lineal interpretable
    - RF: 100 árboles (aprovecha 8 cores), max_depth=10 para capturar patrones
    - SVM: SGDClassifier (única opción viable con 10M registros, mantiene precisión)
    
    Hardware: 16GB RAM, 8 núcleos
    Tiempo estimado: 20-25 minutos total
    """
    modelos = {
        'logreg': {
            'nombre': 'Regresión Logística',
            'clase': lambda seed: LogisticRegression(
                penalty='l2',
                C=1.0,
                max_iter=1000, 
                solver='lbfgs', 
                random_state=seed,
                n_jobs=8  # Usa tus 8 núcleos explícitamente
            )
        },
        'rf': {
            'nombre': 'Random Forest',
            'clase': lambda seed: RandomForestClassifier(
                n_estimators=100,         # Mantiene 100 árboles (máxima precisión)
                max_depth=10,             # Mantiene profundidad 10
                min_samples_split=100,    
                min_samples_leaf=50,
                max_features='sqrt',      # sqrt(13) ≈ 3 features por split (óptimo)
                random_state=seed,
                n_jobs=8,                 # Usa tus 8 núcleos
                verbose=1                 # Muestra progreso
            )
        },
        'svm': {
            'nombre': 'SVM-SGD',
            'clase': lambda seed: SGDClassifier(
                loss='hinge',             # SVM loss
                penalty='l2',
                alpha=0.0001,             
                max_iter=2000,            # Aumentado para convergencia completa
                tol=1e-4,                 # Tolerancia más estricta
                learning_rate='optimal',  # Ajusta learning rate automáticamente
                early_stopping=True,      # Para cuando converge
                validation_fraction=0.1,  # Usa 10% para early stopping
                random_state=seed,
                n_jobs=8                  # Usa tus 8 núcleos
            )
        }
    }
    
    return modelos
