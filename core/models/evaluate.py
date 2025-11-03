from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def evaluar_en_test(train_val_df, test_df, features, modelo_class, modelo_nombre, seed=42):
    print(f"\n{'='*60}")
    print(f"Evaluación en Test: {modelo_nombre}")
    print(f"{'='*60}")
    
    # Datos
    X_train = train_val_df[features].values
    y_train = train_val_df['target'].values
    X_test = test_df[features].values
    y_test = test_df['target'].values
    
    print(f"  Reentrenando en {len(train_val_df):,} ejemplos (85%)...")
    
    # Escalar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Entrenar
    modelo = modelo_class(seed)
    modelo.fit(X_train_scaled, y_train)
    
    # Predecir
    y_pred = modelo.predict(X_test_scaled)
    y_proba = modelo.predict_proba(X_test_scaled)[:, 1]
    
    # Métricas
    cm = confusion_matrix(y_test, y_pred)
    
    metricas = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'balanced_accuracy': float(balanced_accuracy_score(y_test, y_pred)),
        'f1': float(f1_score(y_test, y_pred, zero_division=0)),
        'roc_auc': float(roc_auc_score(y_test, y_proba)),
        'confusion_matrix': cm.tolist(),
        'baseline_accuracy': float(max((y_test == 0).mean(), (y_test == 1).mean())),
        'n_test': len(y_test),
        'n_train': len(y_train)
    }
    
    print(f"\n  Evaluando en {len(test_df):,} ejemplos (15%)...")
    print(f"    Accuracy:          {metricas['accuracy']:.4f}")
    print(f"    Balanced Accuracy: {metricas['balanced_accuracy']:.4f}")
    print(f"    F1-Score:          {metricas['f1']:.4f}")
    print(f"    ROC-AUC:           {metricas['roc_auc']:.4f}")
    print(f"    Baseline:          {metricas['baseline_accuracy']:.4f}")
    print(f"\n  Confusion Matrix:")
    print(f"    [[{cm[0,0]:7d}, {cm[0,1]:7d}]")
    print(f"     [{cm[1,0]:7d}, {cm[1,1]:7d}]]")
    print(f"    (TN, FP)")
    print(f"    (FN, TP)")
    
    return metricas, cm
