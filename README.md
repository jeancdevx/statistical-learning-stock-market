# Proyecto de Aprendizaje Estadístico: Clasificación Binaria en el Mercado NYSE

Proyecto académico de clasificación binaria para predecir si el precio de apertura del día siguiente será mayor que el precio de cierre del día actual en acciones del NYSE.

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Obtención del Dataset](#obtención-del-dataset)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Resultados](#resultados)
- [Detalles Técnicos](#detalles-técnicos)

## 📖 Descripción del Proyecto

Este proyecto implementa la **Sección 5.1: Aplicación al Modelo** del curso de Aprendizaje Estadístico, desarrollando un sistema de clasificación binaria para el mercado de valores NYSE.

**Objetivo**: Predecir si `Open_{t+1} > Close_t` utilizando features técnicos derivados de datos históricos.

**Modelos implementados**:
- Regresión Logística (L2 regularization)
- SVM con kernel RBF

**Protocolo de validación**:
- Split temporal: 75% train / 10% validation / 15% test
- Walk-forward cross-validation (k=5) en el conjunto de validación
- Evaluación única en el conjunto de test

## 🔧 Requisitos Previos

- **Python**: 3.8 o superior (proyecto desarrollado con Python 3.13.7)
- **Sistema operativo**: Windows, macOS o Linux
- **Espacio en disco**: ~5 GB (3 GB para datos crudos + 2.8 GB para dataset procesado)
- **RAM**: Mínimo 8 GB recomendado para procesar 10M+ registros

## 🚀 Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/jeancdevx/statistical-learning-stock-market.git
cd statistical-learning-stock-market
```

### 2. Crear entorno virtual

**En Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

Las dependencias principales son:
- `pandas`: Manipulación de datos
- `numpy`: Operaciones numéricas
- `scikit-learn`: Modelos de ML y métricas
- `matplotlib`: Visualizaciones

## 📊 Obtención del Dataset

### Opción 1: Descarga Manual (Recomendada)

Debido a que el sitio de Stooq tiene protección CAPTCHA, se requiere descarga manual:

1. **Ir al sitio de Stooq**: https://stooq.com/db/h/

2. **Descargar el archivo**: 
   - Buscar "U.S. stocks - daily (ASCII)"
   - Descargar `d_us_txt.zip` (~500 MB)

3. **Extraer el dataset**:

**En Windows (PowerShell)**:
```powershell
# Crear directorio
New-Item -ItemType Directory -Force -Path datasets\nyse

# Copiar el archivo descargado
Copy-Item Downloads\d_us_txt.zip datasets\nyse\

# Extraer
Expand-Archive -Path datasets\nyse\d_us_txt.zip -DestinationPath datasets\nyse\ -Force
```

**En macOS/Linux**:
```bash
# Crear directorio
mkdir -p datasets/nyse

# Copiar el archivo descargado
cp ~/Downloads/d_us_txt.zip datasets/nyse/

# Extraer
cd datasets/nyse
unzip d_us_txt.zip
cd ../..
```

4. **Verificar la extracción**:

```powershell
python verificar_dataset.py
```

Deberías ver:
```
Archivos encontrados en NYSE: 3,649
Ejemplo de archivo: datasets/nyse/data/daily/us/nyse stocks/a.us.txt
```

## 📁 Estructura del Proyecto

```
proyecto/
│
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias de Python
├── .gitignore                        # Archivos excluidos de Git
├── verificar_dataset.py              # Script de verificación del dataset
│
├── datasets/                         # Datos (no incluidos en Git)
│   ├── nyse/                        # Datos crudos de Stooq
│   │   └── data/daily/us/nyse stocks/  # 3,649 archivos .txt
│   └── processed/                   # Datos procesados
│       └── dataset_modelado.csv     # Dataset consolidado (2.8 GB)
│
├── core/
│   ├── data/
│   │   └── make_dataset.py          # Construcción del dataset
│   ├── models/
│   │   └── train_eval.py            # Entrenamiento y evaluación
│   └── utils/                       # Utilidades (futuro)
│
├── reports/
│   ├── metrics/                     # Métricas en formato CSV/JSON
│   │   ├── val_cv_summary_logreg.csv
│   │   ├── val_cv_summary_svm.csv
│   │   ├── test_metrics_logreg.json
│   │   └── test_metrics_svm.json
│   └── figures/                     # Visualizaciones
│       ├── confusion_matrix_logreg.png
│       └── confusion_matrix_svm.png
│
└── app/                             # Aplicación (futuro)
```

## ▶️ Ejecución del Proyecto

### Paso 1: Construir el Dataset

Este paso transforma los 3,649 archivos individuales de acciones en un único CSV consolidado con features y labels.

```powershell
python core/data/make_dataset.py
```

**Tiempo estimado**: 15-25 minutos

**Salida esperada**:
```
============================================================
PASO 1: Construcción del Dataset (5.1)
============================================================

Leyendo archivos desde: datasets/nyse/data/daily/us/nyse stocks
Archivos .txt encontrados: 3,649

Procesando acciones...
  [████████████████████████████████████████] 3649/3649

✓ Acciones válidas: 2,872 (78.7%)
  - Con datos insuficientes: 777

Construyendo features técnicos...
  ✓ Features construidos: 13 indicadores

Aplicando split temporal (75/10/15)...
  ✓ Train: 7,779,738 (75.0%)
  ✓ Val:   1,036,951 (10.0%)
  ✓ Test:  1,557,855 (15.0%)

Balance de clases:
  Train - Clase 0: 4,017,096 (51.63%) / Clase 1: 3,762,642 (48.37%)
  Val   - Clase 0: 535,531 (51.64%) / Clase 1: 501,420 (48.36%)
  Test  - Clase 0: 757,257 (48.61%) / Clase 1: 800,598 (51.39%)

✓ Dataset consolidado: 10,374,544 registros
  Guardado en: datasets\processed\dataset_modelado.csv (2832.9 MB)
```

**Features generados** (13 indicadores técnicos):
1. `ret_cc_1`: Retorno close-to-close
2. `ret_oo_1`: Retorno open-to-open
3. `ret_co_1`: Retorno close-to-open
4. `sma_5`: Media móvil simple (5 días)
5. `sma_10`: Media móvil simple (10 días)
6. `ema_10`: Media móvil exponencial (10 días)
7. `mom_5`: Momentum (5 días)
8. `std_5`: Volatilidad (desviación estándar 5 días)
9. `std_10`: Volatilidad (desviación estándar 10 días)
10. `range_rel`: Rango relativo (High-Low)/Close
11. `vol_ma_10`: Media móvil de volumen (10 días)
12. `vol_rel`: Volumen relativo
13. `dow`: Día de la semana (1=Lunes, 5=Viernes)

**Target**: `y_{t+1} = 1[Open_{t+1} > Close_t]`

### Paso 2: Entrenar y Evaluar Modelos

Este paso entrena los modelos con walk-forward validation y evalúa en el conjunto de test.

```powershell
python core/models/train_eval.py
```

**Tiempo estimado**: 20-35 minutos
- Regresión Logística: ~5 minutos
- SVM-RBF: ~20-30 minutos (kernel no lineal es computacionalmente intensivo)

**Proceso**:
1. Carga del dataset (1-2 minutos)
2. Para cada modelo:
   - **Walk-forward validation** (k=5):
     - Fold 1: Entrena en train (75%), valida en val[0:20%]
     - Fold 2: Entrena en train + val[0:20%], valida en val[20:40%]
     - Fold 3: Entrena en train + val[0:40%], valida en val[40:60%]
     - Fold 4: Entrena en train + val[0:60%], valida en val[60:80%]
     - Fold 5: Entrena en train + val[0:80%], valida en val[80:100%]
   - **Test evaluation**: Entrena en train + val (85%), evalúa UNA VEZ en test (15%)

**Salida esperada**:
```
============================================================
PASO 3: Entrenamiento y Evaluación (5.1)
============================================================

Cargando dataset desde: datasets\processed\dataset_modelado.csv
✓ Dataset cargado: 10,374,544 registros

Distribución:
  Train: 7,779,738 (75.0%)
  Val:   1,036,951 (10.0%)
  Test:  1,557,855 (15.0%)

Features: 13

############################################################
# MODELO: Regresión Logística
############################################################

============================================================
Validación Walk-Forward: Regresión Logística (k=5)
============================================================
  Fold 1/5: acc=0.5234, bacc=0.5234, f1=0.5189, auc=0.5723
  Fold 2/5: acc=0.5241, bacc=0.5240, f1=0.5197, auc=0.5730
  Fold 3/5: acc=0.5238, bacc=0.5237, f1=0.5193, auc=0.5726
  Fold 4/5: acc=0.5235, bacc=0.5234, f1=0.5190, auc=0.5722
  Fold 5/5: acc=0.5232, bacc=0.5231, f1=0.5187, auc=0.5719

Resumen de validación:
  Accuracy:          0.5236 ± 0.0003
  Balanced Accuracy: 0.5235 ± 0.0003
  F1-Score:          0.5191 ± 0.0003
  ROC-AUC:           0.5724 ± 0.0004

  ✓ Guardado: reports/metrics/val_cv_summary_logreg.csv

============================================================
Evaluación en Test: Regresión Logística
============================================================
  Reentrenando en 8,816,689 ejemplos (85%)...
  
  Evaluando en 1,557,855 ejemplos (15%)...
    Accuracy:          0.5240
    Balanced Accuracy: 0.5239
    F1-Score:          0.5265
    ROC-AUC:           0.5732
    Baseline:          0.5139

  Confusion Matrix:
    [[ 394521,  362736]
     [ 379301,  421297]]
    (TN, FP)
    (FN, TP)

  ✓ Guardado: reports/metrics/test_metrics_logreg.json
  ✓ Guardado: reports/figures/confusion_matrix_logreg.png

############################################################
# MODELO: SVM-RBF
############################################################

[Similar output for SVM...]

============================================================
¡Entrenamiento completado!
============================================================
```

## 📈 Resultados

Los resultados se guardan en el directorio `reports/`:

### Métricas de Validación (CSV)

`reports/metrics/val_cv_summary_logreg.csv`:
```csv
fold,accuracy,balanced_accuracy,f1,roc_auc
1,0.5234,0.5234,0.5189,0.5723
2,0.5241,0.5240,0.5197,0.5730
...
```

### Métricas de Test (JSON)

`reports/metrics/test_metrics_logreg.json`:
```json
{
  "accuracy": 0.5240,
  "balanced_accuracy": 0.5239,
  "f1": 0.5265,
  "roc_auc": 0.5732,
  "confusion_matrix": [[394521, 362736], [379301, 421297]],
  "baseline_accuracy": 0.5139,
  "n_test": 1557855,
  "n_train": 8816689,
  "validacion": {
    "accuracy_mean": 0.5236,
    "accuracy_std": 0.0003,
    ...
  }
}
```

### Matrices de Confusión (PNG)

Las matrices de confusión se guardan como imágenes en `reports/figures/`:
- `confusion_matrix_logreg.png`
- `confusion_matrix_svm.png`

## 🔬 Detalles Técnicos

### Dataset

- **Fuente**: Stooq U.S. Daily (ASCII) - NYSE stocks
- **Período**: 1962-01-16 a 2025-10-31 (63 años)
- **Tickers**: 3,649 archivos → 2,872 válidos (con datos suficientes)
- **Registros totales**: 10,374,544
- **Tamaño**: 2.8 GB (CSV)

### Preprocesamiento

1. **Filtrado**: 
   - Eliminación de tickers con < 100 registros
   - Eliminación de registros con NaN en features

2. **Feature Engineering**:
   - Retornos logarítmicos
   - Medias móviles (SMA, EMA)
   - Indicadores de momentum y volatilidad
   - Features de volumen
   - Protección contra división por cero (infinitos → NaN)

3. **Split Temporal**:
   - Por ticker para preservar series temporales
   - Train (75%): Primeros 75% de datos de cada ticker
   - Validation (10%): Siguiente 10% de datos
   - Test (15%): Últimos 15% de datos

### Modelos

**Regresión Logística**:
- Regularización L2 (C=1.0)
- Solver: LBFGS
- Max iterations: 1000
- Random state: 42

**SVM-RBF**:
- Kernel: RBF (Radial Basis Function)
- C=1.0
- Gamma: 'scale'
- Probability: True (para obtener probabilidades)
- Random state: 42

### Protocolo Anti-Leakage

✅ **Garantías de no filtración de información**:

1. **Split temporal**: Los datos de test son cronológicamente posteriores a train/val
2. **StandardScaler**: 
   - `fit()` solo en train
   - `transform()` en val y test
3. **Walk-forward validation**:
   - Cada fold solo usa datos pasados para entrenar
   - Nunca se usa información futura
4. **Sin tuning en test**: 
   - Test se evalúa UNA SOLA VEZ
   - No hay optimización de hiperparámetros en este proyecto

### Métricas

- **Accuracy**: Precisión global
- **Balanced Accuracy**: Promedio de recall por clase (importante para clases balanceadas)
- **F1-Score**: Media armónica de precision y recall
- **ROC-AUC**: Área bajo la curva ROC (capacidad de discriminación)
- **Baseline**: Máximo entre clase mayoritaria (para comparación)

## 🐛 Troubleshooting

### Error: "Module 'pandas' not found"

**Solución**: Asegúrate de tener el entorno virtual activado e instalar dependencias:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Error: "Input X contains infinity"

**Solución**: Este error ya fue corregido en `make_dataset.py`. Si persiste:
```powershell
# Regenerar el dataset
python core/data/make_dataset.py
```

### Error: "No such file or directory: datasets/nyse/"

**Solución**: Asegúrate de haber descargado y extraído el dataset de Stooq en el directorio correcto.

### Proceso muy lento

**Para SVM**: El kernel RBF es computacionalmente intensivo con 10M+ registros. Esto es normal y puede tomar 20-30 minutos.

**Alternativa**: Si necesitas resultados más rápidos para pruebas, puedes modificar `train_eval.py` temporalmente para usar solo un subset de datos:
```python
# En la función main(), después de cargar el dataset:
df = df.sample(frac=0.1, random_state=42)  # Usar solo 10% de datos
```

### Problemas de memoria

**Solución**: Si tienes < 8 GB de RAM, considera:
1. Cerrar otras aplicaciones
2. Usar el subset de datos mencionado arriba
3. Procesar un modelo a la vez (comentar uno en `train_eval.py`)

## 📚 Referencias

- **Stooq Database**: https://stooq.com/db/h/
- **Scikit-learn Documentation**: https://scikit-learn.org/
- **Proyecto académico**: Sección 5.1 - Aplicación al Modelo

## 👥 Autores

Proyecto desarrollado para el curso de Aprendizaje Estadístico.

## 📄 Licencia

Este proyecto es para uso académico únicamente.

---

**Última actualización**: Noviembre 2025

**Estado del proyecto**: ✅ Dataset construido | 🔄 Entrenamiento en progreso
