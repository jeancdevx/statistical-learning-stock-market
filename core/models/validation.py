import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    roc_auc_score
)


def validacion_walk_forward(train_df, val_df, features, modelo_class, modelo_nombre, k=5, seed=42):
    print(f"\n{'='*60}")
    print(f"Validación Walk-Forward: {modelo_nombre} (k={k})")
    print(f"{'='*60}")
    
    # Ordenar val por fecha
    val_df = val_df.sort_values(['Ticker', 'Date']).reset_index(drop=True)
    
    # Datos de train (base)
    X_train_base = train_df[features].values
    y_train_base = train_df['target'].values
    
    # Crear scaler con train
    scaler = StandardScaler()
    scaler.fit(X_train_base)
    
    # Dividir validación en k bloques
    n_val = len(val_df)
    fold_size = n_val // k
    
    metricas_folds = []
    
    for j in range(k):
        # Bloque de validación actual
        val_start = j * fold_size
        val_end = (j + 1) * fold_size if j < k - 1 else n_val
        
        # Datos de validación del fold
        X_val_fold = val_df.iloc[val_start:val_end][features].values
        y_val_fold = val_df.iloc[val_start:val_end]['target'].values
        
        # Datos de entrenamiento: train + val anteriores
        if j == 0:
            # Primer fold: solo train
            X_train_fold = X_train_base
            y_train_fold = y_train_base
        else:
            # Folds posteriores: train + val[0:j]
            X_val_prev = val_df.iloc[:val_start][features].values
            y_val_prev = val_df.iloc[:val_start]['target'].values
            X_train_fold = np.vstack([X_train_base, X_val_prev])
            y_train_fold = np.concatenate([y_train_base, y_val_prev])
        
        # Escalar
        X_train_scaled = scaler.transform(X_train_fold)
        X_val_scaled = scaler.transform(X_val_fold)
        
        # Entrenar
        modelo = modelo_class(seed)
        modelo.fit(X_train_scaled, y_train_fold)
        
        # Predecir
        y_pred = modelo.predict(X_val_scaled)
        y_proba = modelo.predict_proba(X_val_scaled)[:, 1]
        
        # Métricas
        metricas = {
            'fold': j + 1,
            'accuracy': accuracy_score(y_val_fold, y_pred),
            'balanced_accuracy': balanced_accuracy_score(y_val_fold, y_pred),
            'f1': f1_score(y_val_fold, y_pred, zero_division=0),
            'roc_auc': roc_auc_score(y_val_fold, y_proba)
        }
        metricas_folds.append(metricas)
        
        print(f"  Fold {j+1}/{k}: acc={metricas['accuracy']:.4f}, "
              f"bacc={metricas['balanced_accuracy']:.4f}, "
              f"f1={metricas['f1']:.4f}, "
              f"roc_auc={metricas['roc_auc']:.4f}")
    
    # Promedios
    acc_mean = np.mean([m['accuracy'] for m in metricas_folds])
    acc_std = np.std([m['accuracy'] for m in metricas_folds])
    bacc_mean = np.mean([m['balanced_accuracy'] for m in metricas_folds])
    bacc_std = np.std([m['balanced_accuracy'] for m in metricas_folds])
    f1_mean = np.mean([m['f1'] for m in metricas_folds])
    f1_std = np.std([m['f1'] for m in metricas_folds])
    roc_mean = np.mean([m['roc_auc'] for m in metricas_folds])
    roc_std = np.std([m['roc_auc'] for m in metricas_folds])
    
    print(f"\n  PROMEDIO:")
    print(f"    Accuracy:          {acc_mean:.4f} ± {acc_std:.4f}")
    print(f"    Balanced Accuracy: {bacc_mean:.4f} ± {bacc_std:.4f}")
    print(f"    F1-Score:          {f1_mean:.4f} ± {f1_std:.4f}")
    print(f"    ROC-AUC:           {roc_mean:.4f} ± {roc_std:.4f}")
    
    return metricas_folds, {
        'accuracy_mean': acc_mean,
        'accuracy_std': acc_std,
        'balanced_accuracy_mean': bacc_mean,
        'balanced_accuracy_std': bacc_std,
        'f1_mean': f1_mean,
        'f1_std': f1_std,
        'roc_auc_mean': roc_mean,
        'roc_auc_std': roc_std
    }
