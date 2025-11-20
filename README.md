# 📈 Proyecto de Aprendizaje Estadístico: Predicción NYSE

Proyecto académico de clasificación binaria para predecir la dirección del gap overnight (Open_{t+1} > Close_t) en acciones del NYSE utilizando indicadores técnicos y machine learning.

> **Universidad Privada Antenor Orrego**  
> Curso: Aprendizaje Estadístico  
> Docente: Hernan Sagastegui Chigne

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Guía de Instalación Paso a Paso](#-guía-de-instalación-paso-a-paso)
- [Obtención del Dataset](#-obtención-del-dataset)
- [Construcción del Dataset de Modelado](#-construcción-del-dataset-de-modelado)
- [Entrenamiento de Modelos](#-entrenamiento-de-modelos)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Resultados Obtenidos](#-resultados-obtenidos)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Troubleshooting](#-troubleshooting)

## 📖 Descripción del Proyecto

Este proyecto implementa un sistema completo de clasificación binaria para predecir gaps overnight en el mercado de valores NYSE. El objetivo es determinar si el precio de apertura del día siguiente será mayor que el precio de cierre del día actual: **y_{t+1} = 1[Open_{t+1} > Close_t]**.

### **¿Qué predecimos?**
- **Clase 0**: El precio de apertura será menor o igual al cierre anterior (no hay subida overnight)
- **Clase 1**: El precio de apertura será mayor al cierre anterior (subida overnight)

### **Features Utilizados**
13 indicadores técnicos derivados de datos OHLCV:
- **Retornos**: ret_cc_1, ret_oo_1, ret_co_1
- **Tendencia**: sma_5, sma_10, ema_10, mom_5
- **Volatilidad**: std_5, std_10, range_rel
- **Volumen**: vol_ma_10, vol_rel
- **Calendario**: dow (día de la semana)

### **Modelos Implementados**
- **Regresión Logística** con regularización L2
- **Random Forest** (100 árboles, profundidad 10)
- **SVM-SGD** con loss log_loss

### **Protocolo de Validación**
- Split temporal: 75% train / 10% validation / 15% test
- Walk-forward cross-validation (k=5) respetando temporalidad
- Evaluación final en conjunto de test independiente

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior** (proyecto desarrollado con Python 3.13.7)
  - Verificar: `python --version`
- **Git** para clonar el repositorio
- **PowerShell** (Windows) o Terminal (macOS/Linux)
- **Espacio en disco**: ~6 GB libres
  - 500 MB para datos crudos comprimidos
  - 3 GB para datos crudos descomprimidos
  - 2.8 GB para dataset procesado
- **RAM**: Mínimo 8 GB recomendado (procesa 10.4 millones de registros)

## 🚀 Guía de Instalación Paso a Paso

### **Paso 1: Clonar el Repositorio**

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/jeancdevx/statistical-learning-stock-market.git
cd statistical-learning-stock-market
```

### **Paso 2: Crear Entorno Virtual**

Es **importante** usar un entorno virtual para evitar conflictos de dependencias.

**En Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Si obtienes error de ejecución de scripts, ejecuta primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**En macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

Deberías ver `(venv)` al inicio de tu prompt indicando que el entorno está activo.

### **Paso 3: Instalar Dependencias**

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Esto instalará:
- `pandas==2.2.3` - Manipulación de datos tabulares
- `numpy==2.1.3` - Operaciones numéricas
- `scikit-learn==1.5.2` - Algoritmos de ML y métricas
- `matplotlib==3.9.2` - Visualizaciones
- `pyarrow==18.1.0` - Soporte para formato Parquet (optimización de carga)
- `fastapi==0.104.1` - Framework web para API REST
- `uvicorn[standard]==0.24.0` - Servidor ASGI
- `python-multipart==0.0.6` - Manejo de formularios multipart
- `pydantic==2.5.0` - Validación de datos

**Verificar instalación**:
```bash
pip list
```

Deberías ver todas las dependencias listadas.

## 📊 Obtención del Dataset

### **Opción 1: Descarga Manual desde Stooq (Recomendada)**

El sitio de Stooq requiere interacción humana (CAPTCHA), por lo que debes descargar manualmente:

#### **1.1. Descargar el archivo**

1. Ve a: https://stooq.com/db/h/
2. Busca la sección **"U.S. stocks - daily (ASCII)"**
3. Haz clic en **"Download"** para descargar `d_us_txt.zip` (~500 MB)
4. Guarda el archivo en tu carpeta de **Descargas**

#### **1.2. Extraer en el proyecto**

**En Windows (PowerShell)**:
```powershell
# Crear directorio para datos
New-Item -ItemType Directory -Force -Path datasets\nyse

# Copiar el ZIP descargado (ajusta la ruta si es necesario)
Copy-Item $env:USERPROFILE\Downloads\d_us_txt.zip datasets\nyse\

# Extraer
Expand-Archive -Path datasets\nyse\d_us_txt.zip -DestinationPath datasets\nyse\ -Force

# Verificar
Get-ChildItem datasets\nyse\data\daily\us\
```

**En macOS/Linux**:
```bash
# Crear directorio
mkdir -p datasets/nyse

# Copiar el ZIP descargado
cp ~/Downloads/d_us_txt.zip datasets/nyse/

# Extraer
cd datasets/nyse
unzip d_us_txt.zip

# Volver a raíz
cd ../..

# Verificar
ls -la datasets/nyse/data/daily/us/
```

Deberías ver carpetas como:
- `nasdaq etfs/`
- `nasdaq stocks/`
- `nyse etfs/`
- `nyse stocks/` ← **Esta es la que usaremos**
- `nysemkt etfs/`
- `nysemkt stocks/`

### **Opción 2: Si Ya Tienes los Datos**

Si otro miembro del equipo ya descargó los datos, simplemente copia la carpeta `datasets/nyse/` a tu proyecto:

```bash
# Ejemplo: copiar desde un compañero
cp -r /ruta/del/compañero/datasets/nyse ./datasets/
```

## 🔨 Construcción del Dataset de Modelado

Una vez que tengas los datos crudos, debes construir el dataset de modelado con los features técnicos.

### **Ejecutar el Script de Construcción**

**Con el entorno virtual activado**:

**En Windows (PowerShell)**:
```powershell
.\venv\Scripts\python.exe core/data/make_dataset.py
```

**En macOS/Linux**:
```bash
./venv/bin/python core/data/make_dataset.py
```

### **Qué Hace Este Script**

1. **Lee 3,649 archivos** `.txt` de la carpeta `nyse stocks/`
2. **Procesa cada ticker**:
   - Convierte fechas
   - Calcula 13 indicadores técnicos
   - Construye la variable objetivo (target)
   - Aplica ventanas de warm-up
3. **Consolida** todos los tickers en un DataFrame único
4. **Divide temporalmente** en train (75%) / val (10%) / test (15%)
5. **Guarda** el resultado en `datasets/processed/dataset_modelado.csv`

### **Tiempo Estimado**
- **8-12 minutos** dependiendo de tu CPU
- Procesará ~3,600 archivos mostrando progreso cada 500

### **Salida Esperada**

```
============================================================
PASO 2: Construcción del Dataset de Modelado
============================================================

Archivos encontrados: 3649

Procesando tickers...
  Procesados: 500/3649 tickers...
  Procesados: 1000/3649 tickers...
  ...
  Procesados: 3649/3649 tickers...

Consolidando dataset...
✓ Dataset consolidado: 10,374,544 registros

Realizando split temporal 75% / 10% / 15%...

============================================================
RESUMEN DEL DATASET
============================================================
Total de registros: 10,374,544
Tickers únicos: 2872
Rango de fechas: 1962-01-16 a 2025-10-31

Distribución por split:
  train: 7,779,738 (74.99%)
  val  : 1,036,951 (10.00%)
  test : 1,557,855 (15.02%)

Balance de clases (global):
  Clase 0: 5,356,127 (51.63%)
  Clase 1: 5,018,417 (48.37%)

✓ Dataset guardado: datasets\processed\dataset_modelado.csv
  Tamaño: 2832.9 MB

============================================================
✓ PASO 2 COMPLETADO
============================================================
```

### **Verificar que el Dataset se Creó**

```powershell
# Windows
Test-Path datasets\processed\dataset_modelado.csv

# macOS/Linux
ls -lh datasets/processed/dataset_modelado.csv
```

Deberías ver un archivo de aproximadamente **2.8 GB**.

### **⚡ Optimización con Parquet (Recomendado)**

Para mejorar drásticamente el rendimiento de carga del dataset (de 30s a 2-3s), convierte el CSV a formato Parquet:

**Ejecutar una sola vez**:

```bash
python convert_to_parquet.py
```

**Salida esperada**:
```
📄 Leyendo CSV: datasets\processed\dataset_modelado.csv
   Tamaño: 2832.86 MB
✓ CSV cargado en 27.88 segundos
   Registros: 10,374,544

💾 Guardando Parquet: datasets\processed\dataset_modelado.parquet
✓ Parquet guardado en 6.49 segundos
   Tamaño: 1210.41 MB

🚀 Probando velocidad de carga Parquet...
✓ Parquet cargado en 2.46 segundos

📊 Mejora de velocidad: 11.3x más rápido
   CSV:     27.88s
   Parquet: 2.46s

💽 Comparación de tamaño:
   CSV:     2832.86 MB
   Parquet: 1210.41 MB (57.3% más pequeño)

✅ Conversión completada exitosamente!
```

**Beneficios del formato Parquet**:
- ⚡ **11.3x más rápido**: 2.5s vs 30s de carga
- 💾 **57% más pequeño**: 1.2 GB vs 2.8 GB
- 🔧 **Tipos preservados**: No requiere conversión de dtypes
- 📦 **Compresión automática**: Snappy compression
- 🚀 **Optimizado para Big Data**: Formato columnar usado en producción

El sistema detecta automáticamente si existe el archivo Parquet y lo usa preferentemente. Si no existe, usa el CSV como fallback.

## 🎯 Entrenamiento de Modelos

Una vez que tengas el dataset procesado (y opcionalmente convertido a Parquet), puedes entrenar los modelos.

### **Comando Principal**

**Con el entorno virtual activado**:

**En Windows (PowerShell)**:
```powershell
.\venv\Scripts\python.exe train_models.py
```

**En macOS/Linux**:
```bash
./venv/bin/python train_models.py
```

### **Opciones Disponibles**

```bash
# Ver ayuda
python train_models.py --help

# Entrenar todos los modelos (por defecto)
python train_models.py

# Entrenar solo un modelo específico
python train_models.py --models logreg

# Entrenar dos modelos
python train_models.py --models logreg rf

# Cambiar número de folds (por defecto: 5)
python train_models.py --k-folds 3

# Especificar dataset personalizado
python train_models.py --dataset /ruta/al/dataset.csv
```

### **Tiempo Estimado de Entrenamiento**

El proceso completo tarda aproximadamente **1 hora 40 minutos**:

| Modelo | Tiempo Estimado |
|--------|-----------------|
| Logistic Regression | ~2 minutos |
| Random Forest | ~1 hora 37 minutos |
| SVM-SGD | ~3 minutos |

**¿Por qué Random Forest tarda tanto?**
- Entrena 100 árboles de decisión
- Walk-forward CV con k=5 folds (5 entrenamientos)
- Procesa 10.4 millones de registros
- Usa 8 núcleos en paralelo (configurable en `settings.py`)

### **Salida del Entrenamiento**

Verás algo como esto:

```
======================================================================
               PROYECTO: PREDICCIÓN NYSE
          Modelado de Dirección de Precio Overnight
======================================================================

Configuración:
  Dataset:     datasets\processed\dataset_modelado.csv
  K-folds:     5
  Modelos:     Todos
  Features:    13 indicadores técnicos
  Split:       75% / 10% / 15%
  Paralelismo: 8 cores
======================================================================

============================================================
Validación Walk-Forward: Logistic Regression (k=5)
============================================================
  Fold 1/5: acc=0.5072, bacc=0.5037, f1=0.1629, roc_auc=0.5235
  Fold 2/5: acc=0.5107, bacc=0.5006, f1=0.1273, roc_auc=0.5181
  ...

  PROMEDIO:
    Accuracy:          0.5120 ± 0.0050
    ROC-AUC:           0.5204 ± 0.0034

============================================================
Evaluación en Test: Logistic Regression
============================================================
    Accuracy:          0.5156
    ROC-AUC:           0.5131

[... continúa con Random Forest y SVM ...]

======================================================================
RESUMEN FINAL - COMPARACIÓN DE MODELOS
======================================================================

             Modelo  Accuracy  Balanced Acc  F1-Score  ROC-AUC
      Random Forest    0.5369        0.5353    0.5026   0.5549
Logistic Regression    0.5156        0.5025    0.1082   0.5131
            SVM-SGD    0.5150        0.5027    0.1521   0.5123

🏆 MEJOR MODELO: Random Forest
   ROC-AUC: 0.5549
   Accuracy: 0.5369

✅ ENTRENAMIENTO COMPLETADO EXITOSAMENTE
   Resultados guardados en: reports/
```

### **Archivos Generados**

Después del entrenamiento, encontrarás en la carpeta `reports/`:

#### **Métricas (`reports/metrics/`)**:
- `val_cv_summary_logreg.csv` - Resultados CV de Logistic Regression
- `test_metrics_logreg.json` - Métricas finales de Logistic Regression
- `val_cv_summary_rf.csv` - Resultados CV de Random Forest
- `test_metrics_rf.json` - Métricas finales de Random Forest
- `val_cv_summary_svm.csv` - Resultados CV de SVM-SGD
- `test_metrics_svm.json` - Métricas finales de SVM-SGD
- `models_comparison.csv` - Comparación de los 3 modelos

#### **Visualizaciones (`reports/figures/`)**:
- `confusion_matrix_logreg.png` - Matriz de confusión Logistic Regression
- `confusion_matrix_rf.png` - Matriz de confusión Random Forest
- `confusion_matrix_svm.png` - Matriz de confusión SVM-SGD

#### **Modelos Guardados (`models/`)**:
- `model_logreg.pkl` - Modelo serializado Logistic Regression
- `model_rf.pkl` - Modelo serializado Random Forest
- `model_svm.pkl` - Modelo serializado SVM-SGD

## 📊 Interpretación de Resultados

### **Métricas de Validación Walk-Forward**

Cada modelo genera un archivo CSV con los resultados de validación cruzada:

**Ejemplo**: `reports/metrics/val_cv_summary_rf.csv`
```csv
fold,accuracy,balanced_accuracy,f1,roc_auc
1,0.5330,0.5312,0.4989,0.5510
2,0.5339,0.5321,0.4998,0.5519
3,0.5336,0.5318,0.4995,0.5516
4,0.5333,0.5315,0.4992,0.5513
5,0.5330,0.5312,0.4989,0.5510
```

**¿Qué significan las métricas?**

- **Accuracy**: Porcentaje de predicciones correctas (clase 0 y 1)
  - Ejemplo: 0.5330 = 53.30% de predicciones correctas
- **Balanced Accuracy**: Promedio del recall de cada clase
  - Útil cuando las clases están balanceadas (como aquí: ~51% vs ~49%)
- **F1-Score**: Media armónica de precision y recall
  - Balancea falsos positivos y falsos negativos
- **ROC-AUC**: Área bajo la curva ROC
  - Mide capacidad de discriminación entre clases
  - 0.5 = aleatorio, 1.0 = perfecto
  - **0.5549** (Random Forest) indica un modelo ligeramente mejor que el azar

**Estabilidad del modelo**: La desviación estándar pequeña entre folds indica consistencia temporal.

### **Métricas de Test Final**

Después del entrenamiento, cada modelo tiene un archivo JSON con resultados finales:

**Ejemplo**: `reports/metrics/test_metrics_rf.json`
```json
{
  "accuracy": 0.5369,
  "balanced_accuracy": 0.5353,
  "f1": 0.5026,
  "roc_auc": 0.5549,
  "confusion_matrix": [[440123, 317134], [404438, 396160]],
  "baseline_accuracy": 0.4861,
  "n_test": 1557855,
  "n_train": 8816689
}
```

**Interpretación**:
- **ROC-AUC 0.5549**: El modelo es ~5.5 puntos mejor que el azar
- **Accuracy 53.69%**: Predice correctamente en más de la mitad de los casos
- **F1 0.5026**: Balance razonable entre precisión y recall

**Comparación con baseline**:
- Baseline (clase mayoritaria): 48.61%
- Random Forest: 53.69%
- **Mejora relativa**: +5.08 puntos porcentuales

### **Matrices de Confusión**

Las matrices de confusión visuales están en `reports/figures/`:

**Estructura**:
```
                 Predicho
                 0        1
Verdadero  0   [TN]     [FP]
           1   [FN]     [TP]
```

**Ejemplo Random Forest**:
```
                 Predicho
                 0        1
Verdadero  0   440,123  317,134
           1   404,438  396,160
```

**Interpretación**:
- **True Negatives (TN)**: 440,123 casos donde predijo 0 correctamente
- **False Positives (FP)**: 317,134 casos donde predijo 1 incorrectamente
- **False Negatives (FN)**: 404,438 casos donde predijo 0 incorrectamente
- **True Positives (TP)**: 396,160 casos donde predijo 1 correctamente

**Tasa de Aciertos por Clase**:
- Clase 0 (bajadas): 440,123 / (440,123 + 317,134) = 58.1%
- Clase 1 (subidas): 396,160 / (404,438 + 396,160) = 49.5%

**Conclusión**: El modelo es mejor prediciendo bajadas que subidas.

### **Comparación de Modelos**

El archivo `reports/metrics/models_comparison.csv` consolida todos los resultados:

```csv
Modelo,Accuracy,Balanced Acc,F1-Score,ROC-AUC
Random Forest,0.5369,0.5353,0.5026,0.5549
Logistic Regression,0.5156,0.5025,0.1082,0.5131
SVM-SGD,0.5150,0.5027,0.1521,0.5123
```

**Conclusión**: 
- 🏆 **Random Forest es el ganador** con ROC-AUC de 0.5549
- LogReg y SVM-SGD tienen rendimiento similar (~0.515 en accuracy)
- Random Forest tiene mejor F1-Score (0.5026 vs ~0.13)

## 📁 Estructura Completa del Proyecto

```
proyecto/
│
├── README.md                          # 📖 Esta guía completa
├── requirements.txt                   # 📦 Dependencias de Python
├── train_models.py                    # 🚀 CLI para entrenar modelos
├── verificar_dataset.py              # ✅ Script de verificación
│
├── datasets/                          # 📊 Datos (no incluidos en Git)
│   ├── nyse/                         # Datos crudos de Stooq
│   │   └── data/daily/us/
│   │       └── nyse stocks/          # 3,649 archivos .txt
│   │           ├── a.us.txt
│   │           ├── aa.us.txt
│   │           └── ...
│   └── processed/                    # Datos procesados
│       ├── dataset_modelado.csv      # 💾 2.8 GB - 10.4M registros (CSV)
│       └── dataset_modelado.parquet  # ⚡ 1.2 GB - 10.4M registros (Parquet, 11x más rápido)
│
├── core/                              # 🧠 Código principal
│   ├── config/                       # Configuración
│   │   ├── __init__.py
│   │   └── settings.py               # ⚙️ Parámetros centralizados
│   │
│   ├── data/                         # Construcción de datos
│   │   └── make_dataset.py           # 🔨 Genera dataset_modelado.csv
├── convert_to_parquet.py              # ⚡ Convierte CSV a Parquet (opcional)
│   │
│   ├── models/                       # Modelos y evaluación
│   │   ├── __init__.py
│   │   ├── base_model.py             # 🏗️ Clase base abstracta
│   │   ├── logistic_regression.py    # 📈 Implementación LogReg
│   │   ├── random_forest.py          # 🌳 Implementación RF
│   │   ├── svm_sgd.py                # 🔷 Implementación SVM-SGD
│   │   ├── model_factory.py          # 🏭 Patrón Factory
│   │   ├── validation.py             # ✓ Walk-forward CV
│   │   └── evaluate.py               # 📊 Evaluación en test
│   │
│   ├── pipelines/                    # Orquestación
│   │   ├── __init__.py
│   │   └── training_pipeline.py      # 🎯 Pipeline principal
│   │
│   └── utils/                        # Utilidades
│       ├── __init__.py
│       └── visualization.py          # 📉 Matrices de confusión
│
├── models/                            # 💾 Modelos serializados (.pkl)
│   ├── model_logreg.pkl
│   ├── model_rf.pkl
│   └── model_svm.pkl
│
├── reports/                           # 📋 Resultados del entrenamiento
│   ├── metrics/                      # Métricas en CSV/JSON
│   │   ├── val_cv_summary_logreg.csv    # Validación LogReg
│   │   ├── test_metrics_logreg.json     # Test LogReg
│   │   ├── val_cv_summary_rf.csv        # Validación RF
│   │   ├── test_metrics_rf.json         # Test RF
│   │   ├── val_cv_summary_svm.csv       # Validación SVM
│   │   ├── test_metrics_svm.json        # Test SVM
│   │   └── models_comparison.csv        # 📊 Comparación final
│   │
│   └── figures/                      # Visualizaciones PNG
│       ├── confusion_matrix_logreg.png  # Matriz LogReg
│       ├── confusion_matrix_rf.png      # Matriz RF
│       └── confusion_matrix_svm.png     # Matriz SVM
│
├── docs/                              # 📚 Documentación académica
│   ├── Aprendizaje Estadistico - Proyecto - Jeancarlo Morales.md
│   └── Silabo AE 2025-20 - ISIA.md
│
└── app/                               # 🚧 Aplicación futura
```

### **Resumen de Archivos Clave**

| Archivo | Propósito |
|---------|-----------|
| `train_models.py` | Punto de entrada CLI para entrenar modelos |
| `core/config/settings.py` | Configuración centralizada (paths, hiperparámetros) |
| `core/data/make_dataset.py` | Construye dataset de 10.4M registros |
| `core/models/base_model.py` | Clase abstracta con fit/predict/save |
| `core/models/model_factory.py` | Factory para crear modelos dinámicamente |
| `core/models/validation.py` | Walk-forward validation k-fold |
| `core/models/evaluate.py` | Evaluación final en test set |
| `core/pipelines/training_pipeline.py` | Orquestador principal del flujo |
| `reports/metrics/models_comparison.csv` | Comparación final de modelos |

## 🔬 Detalles Técnicos

### **Dataset**

- **Fuente**: Stooq U.S. Daily (ASCII) - NYSE stocks
- **Período**: 1962-01-16 a 2025-10-31 (63 años de historia)
- **Tickers originales**: 3,649 archivos
- **Tickers válidos**: 2,872 (filtrados por datos suficientes)
- **Registros totales**: 10,374,544
- **Tamaño en disco**: 2.8 GB (CSV)
- **Balance de clases**: 51.63% clase 0 / 48.37% clase 1

### **Features Técnicos (13)**

| Feature | Descripción | Fórmula |
|---------|-------------|---------|
| `ret_cc_1` | Retorno close-to-close | $\log(Close_t / Close_{t-1})$ |
| `ret_oo_1` | Retorno open-to-open | $\log(Open_t / Open_{t-1})$ |
| `ret_co_1` | Retorno close-to-open | $\log(Close_t / Open_t)$ |
| `sma_5` | Media móvil simple 5 días | $\frac{1}{5}\sum_{i=0}^{4} Close_{t-i}$ |
| `sma_10` | Media móvil simple 10 días | $\frac{1}{10}\sum_{i=0}^{9} Close_{t-i}$ |
| `ema_10` | Media móvil exponencial 10 | EMA con $\alpha = 2/(10+1)$ |
| `mom_5` | Momentum 5 días | $Close_t - Close_{t-5}$ |
| `std_5` | Volatilidad 5 días | $\sigma(Close_{t-4:t})$ |
| `std_10` | Volatilidad 10 días | $\sigma(Close_{t-9:t})$ |
| `range_rel` | Rango relativo | $(High_t - Low_t) / Close_t$ |
| `vol_ma_10` | Media móvil volumen 10 | $\frac{1}{10}\sum_{i=0}^{9} Volume_{t-i}$ |
| `vol_rel` | Volumen relativo | $Volume_t / vol\_ma\_10_t$ |
| `dow` | Día de la semana | 1=Lunes, 5=Viernes |

**Ventana de warm-up**: 10 días (para calcular features sin NaN)

### **Target (Variable Objetivo)**

$$y_{t+1} = \mathbb{1}[Open_{t+1} > Close_t]$$

- **Clase 0**: El precio de apertura del día siguiente es **menor o igual** que el cierre de hoy (bajada)
- **Clase 1**: El precio de apertura del día siguiente es **mayor** que el cierre de hoy (subida)

**Interpretación**: Predecimos si el precio "saltará" al abrir al día siguiente.

### **Split Temporal**

| Conjunto | Proporción | Registros | Uso |
|----------|------------|-----------|-----|
| **Train** | 75% | 7,779,738 | Entrenamiento inicial |
| **Val** | 10% | 1,036,951 | Walk-forward validation |
| **Test** | 15% | 1,557,855 | Evaluación final (UNA VEZ) |

**Método**: Split temporal por ticker para preservar series temporales.

**Garantía anti-leakage**: 
- StandardScaler fitteado solo en train
- Validación walk-forward usa solo datos pasados
- Test evaluado una sola vez (no hay tuning en test)

### **Protocolo de Validación Walk-Forward**

**k=5 folds**:

1. **Fold 1**: Train en 75% → Evalúa en val[0:20%]
2. **Fold 2**: Train en 75% + val[0:20%] → Evalúa en val[20:40%]
3. **Fold 3**: Train en 75% + val[0:40%] → Evalúa en val[40:60%]
4. **Fold 4**: Train en 75% + val[0:60%] → Evalúa en val[60:80%]
5. **Fold 5**: Train en 75% + val[0:80%] → Evalúa en val[80:100%]

**Ventaja**: Simula trading real donde solo usas datos pasados para predecir el futuro.

### **Hiperparámetros de los Modelos**

#### **Logistic Regression**
```python
LogisticRegression(
    penalty='l2',           # Regularización L2
    C=1.0,                  # Inverso de lambda
    solver='lbfgs',         # Optimizador
    max_iter=1000,          # Máximo de iteraciones
    random_state=42,        # Reproducibilidad
    n_jobs=8                # Paralelismo
)
```

#### **Random Forest**
```python
RandomForestClassifier(
    n_estimators=100,       # 100 árboles
    max_depth=10,           # Profundidad máxima
    min_samples_split=50,   # Mínimo para split
    min_samples_leaf=20,    # Mínimo en hoja
    random_state=42,        # Reproducibilidad
    n_jobs=8                # Paralelismo
)
```

#### **SVM-SGD**
```python
SGDClassifier(
    loss='log_loss',        # Para probabilidades
    penalty='l2',           # Regularización L2
    alpha=0.0001,           # Lambda
    max_iter=2000,          # Máximo de iteraciones
    tol=1e-3,               # Tolerancia de convergencia
    random_state=42,        # Reproducibilidad
    n_jobs=8                # Paralelismo
)
```

### **Métricas de Evaluación**

| Métrica | Fórmula | Interpretación |
|---------|---------|----------------|
| **Accuracy** | $\frac{TP + TN}{TP + TN + FP + FN}$ | Precisión global |
| **Balanced Accuracy** | $\frac{1}{2}\left(\frac{TP}{TP+FN} + \frac{TN}{TN+FP}\right)$ | Promedio de recall por clase |
| **F1-Score** | $2 \cdot \frac{precision \cdot recall}{precision + recall}$ | Media armónica |
| **ROC-AUC** | Área bajo curva ROC | Capacidad de discriminación |

**Baseline**: Siempre predecir la clase mayoritaria (para comparar con modelo trivial).

## 🐛 Solución de Problemas

### **Error: "Module 'pandas' not found"**

**Causa**: Entorno virtual no activado o dependencias no instaladas.

**Solución**:
```powershell
# Windows
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

### **Error: "No such file or directory: datasets/nyse/"**

**Causa**: Datos crudos no descargados o extraídos incorrectamente.

**Solución**:
1. Descarga `d_us_txt.zip` desde https://stooq.com/db/h/
2. Extrae en `datasets/nyse/`
3. Verifica con `python verificar_dataset.py`

### **Error: "No such file: datasets/processed/dataset_modelado.csv"**

**Causa**: Dataset de modelado no construido aún.

**Solución**:
```powershell
python core/data/make_dataset.py
```

### **Error: "MemoryError" durante entrenamiento**

**Causa**: RAM insuficiente para procesar 10.4M registros.

**Solución temporal** (solo para pruebas):

Edita `train_models.py` y agrega después de cargar el dataset:
```python
# Línea 45, después de cargar el dataset
df = df.sample(frac=0.1, random_state=42)  # Usar solo 10%
```

**Solución permanente**:
- Cerrar otras aplicaciones
- Aumentar RAM virtual (swap)
- Ejecutar en máquina con más memoria

### **Entrenamiento muy lento (Random Forest)**

**Causa**: Random Forest con 100 árboles y 10M+ registros es computacionalmente intensivo.

**Esto es normal**: Espera 1h 30min - 2h dependiendo de tu CPU.

**Para acelerar** (sacrificando precisión):

Edita `core/config/settings.py`:
```python
# Línea 45
'n_estimators': 50,     # Reducir de 100 a 50 árboles
'max_depth': 8,         # Reducir profundidad
```

### **Error: "Can't execute PowerShell scripts"**

**Causa**: Política de ejecución de PowerShell restringida.

**Solución**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Advertencia: "DtypeWarning" al cargar dataset**

**Causa**: Advertencia normal de pandas al inferir tipos de datos.

**No requiere acción**: Es solo una advertencia, no afecta el funcionamiento.

### **Error: "FileNotFoundError: reports/metrics/"**

**Causa**: Carpetas de salida no existen aún.

**Solución**: Los scripts las crean automáticamente. Si persiste:
```powershell
# Windows
New-Item -ItemType Directory -Force -Path reports\metrics
New-Item -ItemType Directory -Force -Path reports\figures
New-Item -ItemType Directory -Force -Path models

# macOS/Linux
mkdir -p reports/metrics reports/figures models
```

## 🔍 Verificación Final

Para asegurar que todo funciona correctamente:

### **1. Verificar entorno virtual**
```powershell
# Debería mostrar (venv) al inicio
# Windows
Get-Command python

# macOS/Linux
which python
```

### **2. Verificar dependencias**
```powershell
pip list | Select-String "pandas|numpy|scikit-learn|matplotlib"

# Deberías ver:
# pandas       2.2.3
# numpy        2.1.3
# scikit-learn 1.5.2
# matplotlib   3.9.2
```

### **3. Verificar dataset crudo**
```powershell
python verificar_dataset.py

# Debería mostrar:
# Archivos encontrados en NYSE: 3,649
```

### **4. Verificar dataset procesado**
```powershell
# Windows
Test-Path datasets\processed\dataset_modelado.csv

# macOS/Linux
ls -lh datasets/processed/dataset_modelado.csv

# Debería mostrar: ~2.8 GB
```

### **5. Verificar modelos entrenados**
```powershell
# Windows
Get-ChildItem models\*.pkl

# macOS/Linux
ls -lh models/*.pkl

# Deberías ver 3 archivos:
# model_logreg.pkl
# model_rf.pkl
# model_svm.pkl
```

### **6. Verificar resultados**
```powershell
# Windows
Get-ChildItem reports\metrics\*.csv
Get-ChildItem reports\figures\*.png

# macOS/Linux
ls -lh reports/metrics/*.csv
ls -lh reports/figures/*.png

# Deberías ver:
# 4 archivos CSV (3 val + 1 comparison)
# 3 archivos JSON (test metrics)
# 3 archivos PNG (confusion matrices)
```

## 📚 Referencias y Recursos

### **Dataset**
- **Stooq Database**: https://stooq.com/db/h/
- **Documentación de formato**: https://stooq.com/db/d/

### **Bibliotecas**
- **pandas**: https://pandas.pydata.org/docs/
- **scikit-learn**: https://scikit-learn.org/stable/
- **NumPy**: https://numpy.org/doc/
- **Matplotlib**: https://matplotlib.org/stable/contents.html

### **Metodología**
- **Walk-forward validation**: https://en.wikipedia.org/wiki/Walk_forward_analysis
- **ROC-AUC**: https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics

### **Machine Learning**
- **Logistic Regression**: https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
- **Random Forest**: https://scikit-learn.org/stable/modules/ensemble.html#forest
- **SVM-SGD**: https://scikit-learn.org/stable/modules/sgd.html

### **Proyecto Académico**
- **Documento principal**: `docs/Aprendizaje Estadistico - Proyecto - Jeancarlo Morales.md`
- **Sílabo del curso**: `docs/Silabo AE 2025-20 - ISIA.md`

## 👥 Autores y Contribuciones

**Desarrollador Principal**: Jeancarlo Morales  
**Curso**: Aprendizaje Estadístico 2025-20  
**Institución**: Universidad Privada Antenor Orrego (UPAO)  
**Escuela**: Ingeniería de Sistemas e Informática (ISIA)

### **Contacto**
Para dudas o problemas con el proyecto, contactar a través de:
- **Email**: [jcode2006@gmail.com]
- **GitHub**: [jeancdevx]

## 📄 Licencia

Este proyecto es de uso **académico exclusivo**.

- ❌ No se permite uso comercial
- ✅ Permitido para estudio y aprendizaje
- ✅ Permitido compartir con compañeros del curso
- ❌ No redistribuir públicamente sin permiso

**Nota sobre datos**: El dataset de Stooq está sujeto a sus propios términos de uso. Consultar https://stooq.com/ para más información.

## 📝 Changelog

### **Versión 1.0** (Noviembre 2025)
- ✅ Construcción del dataset (10.4M registros)
- ✅ Implementación de 3 modelos (LogReg, RF, SVM-SGD)
- ✅ Pipeline de entrenamiento completo
- ✅ Walk-forward validation (k=5)
- ✅ Evaluación en test set
- ✅ Visualizaciones (matrices de confusión)
- ✅ Documentación académica (Secciones 5 y 6)
- ✅ README completo con guía paso a paso

### **Futuras Mejoras** (Roadmap)
- 🔄 Aplicación web interactiva (Streamlit/Dash)
- 🔄 Tuning de hiperparámetros con GridSearchCV
- 🔄 Modelos adicionales (XGBoost, LightGBM)
- 🔄 Feature engineering avanzado (RSI, MACD, Bollinger Bands)
- 🔄 Análisis de feature importance
- 🔄 Backtesting con estrategia de trading

---

**🎯 Estado del Proyecto**: ✅ **COMPLETO Y FUNCIONAL**

**Última actualización**: 08 de Noviembre del 2025

**¿Dudas?** Consulta la sección de [Solución de Problemas](#-solución-de-problemas) o contacta al autor.

---

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!**

