import numpy as np
import pandas as pd
from typing import Tuple, Dict
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
from core.models.base_model import BaseModel


def evaluar_en_test(
    model: BaseModel,
    train_val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    features: list
) -> Tuple[Dict, np.ndarray]:
    print(f"\n{'='*60}")
    print(f"Evaluación en Test: {model.name}")
    print(f"{'='*60}")
    
    X_train_val = train_val_df[features]
    y_train_val = train_val_df['target']
    X_test = test_df[features]
    y_test = test_df['target']
    
    print(f"  Reentrenando en {len(train_val_df):,} ejemplos (85%)...")
    
    model.fit(X_train_val, y_train_val)
    
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    cm = confusion_matrix(y_test, y_pred)
    
    metricas = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'balanced_accuracy': float(balanced_accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred, zero_division=0)),
        'recall': float(recall_score(y_test, y_pred, zero_division=0)),
        'f1': float(f1_score(y_test, y_pred, zero_division=0)),
        'roc_auc': float(roc_auc_score(y_test, y_proba)),
        'confusion_matrix': cm.tolist(),
        'baseline_accuracy': float(max((y_test == 0).mean(), (y_test == 1).mean())),
        'n_test': int(len(y_test)),
        'n_train_val': int(len(y_train_val)),
        'class_distribution': {
            'class_0': int((y_test == 0).sum()),
            'class_1': int((y_test == 1).sum())
        }
    }
    
    print(f"\n  Evaluando en {len(test_df):,} ejemplos (15%)...")
    print(f"    Accuracy:          {metricas['accuracy']:.4f}")
    print(f"    Balanced Accuracy: {metricas['balanced_accuracy']:.4f}")
    print(f"    Precision:         {metricas['precision']:.4f}")
    print(f"    Recall:            {metricas['recall']:.4f}")
    print(f"    F1-Score:          {metricas['f1']:.4f}")
    print(f"    ROC-AUC:           {metricas['roc_auc']:.4f}")
    print(f"    Baseline:          {metricas['baseline_accuracy']:.4f}")
    print(f"\n  Confusion Matrix:")
    print(f"    [[{cm[0,0]:7d}, {cm[0,1]:7d}]")
    print(f"     [{cm[1,0]:7d}, {cm[1,1]:7d}]]")
    print(f"    (TN, FP)")
    print(f"    (FN, TP)")
    print(f"\n  Distribución de clases en test:")
    print(f"    Clase 0: {metricas['class_distribution']['class_0']:,}")
    print(f"    Clase 1: {metricas['class_distribution']['class_1']:,}")
    
    return metricas, cm

