"""
Módulo de validación cruzada temporal (Walk-Forward).

Implementa la validación walk-forward específica para series temporales,
respetando el orden temporal y evitando look-ahead bias.
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
from core.models.base_model import BaseModel
from core.config.settings import Settings


def validacion_walk_forward(
    model: BaseModel,
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    features: List[str],
    k: int = None
) -> Tuple[List[Dict], Dict]:
    """
    Realiza validación cruzada walk-forward temporal.
    
    Este método divide el conjunto de validación en k bloques contiguos.
    En cada fold, entrena con los datos históricos (train + folds anteriores)
    y valida en el fold actual, respetando el flujo temporal.
    
    Args:
        model: Instancia del modelo (debe heredar de BaseModel)
        train_df: DataFrame de entrenamiento (75%)
        val_df: DataFrame de validación (10%)
        features: Lista de nombres de features a usar
        k: Número de folds (si None, usa Settings.K_FOLDS)
        
    Returns:
        Tupla de (metricas_folds, metricas_promedio):
            - metricas_folds: Lista de diccionarios con métricas por fold
            - metricas_promedio: Diccionario con medias y desviaciones estándar
            
    Example:
        >>> from core.models import LogisticRegressionModel
        >>> model = LogisticRegressionModel()
        >>> folds, summary = validacion_walk_forward(model, train_df, val_df, features)
    """
    if k is None:
        k = Settings.K_FOLDS
    
    print(f"\n{'='*60}")
    print(f"Validación Walk-Forward: {model.name} (k={k})")
    print(f"{'='*60}")
    
    # Ordenar validación por fecha (asegurar temporalidad)
    val_df = val_df.sort_values(['Ticker', 'Date']).reset_index(drop=True)
    
    # Extraer features y target del conjunto base de entrenamiento
    X_train_base = train_df[features]
    y_train_base = train_df['target']
    
    # Dividir validación en k bloques temporales contiguos
    n_val = len(val_df)
    fold_size = n_val // k
    
    metricas_folds = []
    
    for j in range(k):
        # Definir rango del fold actual
        val_start = j * fold_size
        val_end = (j + 1) * fold_size if j < k - 1 else n_val
        
        # Extraer datos del fold de validación
        X_val_fold = val_df.iloc[val_start:val_end][features]
        y_val_fold = val_df.iloc[val_start:val_end]['target']
        
        # Construir conjunto de entrenamiento acumulativo (walk-forward)
        if j == 0:
            # Primer fold: solo usa el conjunto de entrenamiento base
            X_train_fold = X_train_base
            y_train_fold = y_train_base
        else:
            # Folds posteriores: train base + todos los folds anteriores de validación
            X_val_prev = val_df.iloc[:val_start][features]
            y_val_prev = val_df.iloc[:val_start]['target']
            X_train_fold = pd.concat([X_train_base, X_val_prev], ignore_index=True)
            y_train_fold = pd.concat([y_train_base, y_val_prev], ignore_index=True)
        
        # Entrenar el modelo en el fold
        # Nota: El modelo aplica scaling internamente si requires_scaling=True
        model.fit(X_train_fold, y_train_fold)
        
        # Realizar predicciones
        y_pred = model.predict(X_val_fold)
        y_proba = model.predict_proba(X_val_fold)[:, 1]
        
        # Calcular métricas del fold
        metricas = {
            'fold': j + 1,
            'accuracy': accuracy_score(y_val_fold, y_pred),
            'balanced_accuracy': balanced_accuracy_score(y_val_fold, y_pred),
            'precision': precision_score(y_val_fold, y_pred, zero_division=0),
            'recall': recall_score(y_val_fold, y_pred, zero_division=0),
            'f1': f1_score(y_val_fold, y_pred, zero_division=0),
            'roc_auc': roc_auc_score(y_val_fold, y_proba)
        }
        metricas_folds.append(metricas)
        
        # Imprimir resultados del fold
        print(f"  Fold {j+1}/{k}: "
              f"acc={metricas['accuracy']:.4f}, "
              f"bacc={metricas['balanced_accuracy']:.4f}, "
              f"f1={metricas['f1']:.4f}, "
              f"roc_auc={metricas['roc_auc']:.4f}")
    
    # Calcular estadísticas agregadas (media y desviación estándar)
    metricas_promedio = {}
    for metric_name in ['accuracy', 'balanced_accuracy', 'precision', 'recall', 'f1', 'roc_auc']:
        values = [m[metric_name] for m in metricas_folds]
        metricas_promedio[f'{metric_name}_mean'] = np.mean(values)
        metricas_promedio[f'{metric_name}_std'] = np.std(values)
    
    # Imprimir resumen
    print(f"\n  PROMEDIO:")
    print(f"    Accuracy:          {metricas_promedio['accuracy_mean']:.4f} ± "
          f"{metricas_promedio['accuracy_std']:.4f}")
    print(f"    Balanced Accuracy: {metricas_promedio['balanced_accuracy_mean']:.4f} ± "
          f"{metricas_promedio['balanced_accuracy_std']:.4f}")
    print(f"    Precision:         {metricas_promedio['precision_mean']:.4f} ± "
          f"{metricas_promedio['precision_std']:.4f}")
    print(f"    Recall:            {metricas_promedio['recall_mean']:.4f} ± "
          f"{metricas_promedio['recall_std']:.4f}")
    print(f"    F1-Score:          {metricas_promedio['f1_mean']:.4f} ± "
          f"{metricas_promedio['f1_std']:.4f}")
    print(f"    ROC-AUC:           {metricas_promedio['roc_auc_mean']:.4f} ± "
          f"{metricas_promedio['roc_auc_std']:.4f}")
    
    return metricas_folds, metricas_promedio

