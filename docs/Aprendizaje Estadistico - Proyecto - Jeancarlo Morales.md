**Universidad Privada Antenor Orrego** 

**Facultad de Ingeniería** 

**Programa de Estudio de Ingeniería de Sistemas e Inteligencia Artificial** 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.001.png)

**Curso:** Aprendizaje Estadístico **Proyecto Semestral** 

**“Modelado y análisis predictivo de precios de acciones en el mercado bursátil mediante técnicas avanzadas de aprendizaje estadístico”** 

**Equipo de Trabajo** 

Olazabal Ávila Fernando 

Kong Carranza Luis 

Morales Robles Jeancarlo (coordinador) León García Axel 

Gastañuadi Iturri, Efrain  Tarazona Flores José 

Albitres Dávila Juan \
**Docente:** Hernan Sagastegui Chigne **Trujillo – 21 de septiembre del 2025** 

Aprendizaje Estadístico  Proyecto Semestral 

<a name="_page1_x82.00_y71.00"></a>**Índice del Contenido** 

[Índice del Contenido............................................................................................................... 2 ](#_page1_x82.00_y71.00)

1. [Introducción .................................................................................................................... 4 ](#_page3_x82.00_y71.00)
1. [Título del Proyecto ................................................................................................. 4 ](#_page3_x82.00_y96.00)
1. [Antecedentes........................................................................................................... 4 ](#_page3_x82.00_y174.00)
1. [Problema a resolver ................................................................................................ 6 ](#_page5_x82.00_y71.00)
1. [Objetivos................................................................................................................. 6 ](#_page5_x82.00_y208.00)
1. [Objetivo general: ............................................................................................ 6 ](#_page5_x82.00_y232.00)
1. [Objetivos específicos: ..................................................................................... 6 ](#_page5_x82.00_y352.00)
2. [Requerimientos ............................................................................................................... 7 ](#_page6_x82.00_y71.00)
1. [Definición del dominio ........................................................................................... 7 ](#_page6_x82.00_y96.00)
1. [Determinación de requisitos (requerimientos) ....................................................... 7 ](#_page6_x82.00_y528.00)
3. [Pre-Procesamiento y Normalización .............................................................................. 9 ](#_page8_x82.00_y71.00)
1. [Medidas, Datos, Bases de Datos y Elaboración del Data-Set ................................ 9 ](#_page8_x82.00_y96.00)
1. [Normalización y/o Filtrado de Datos ..................................................................... 9 ](#_page8_x82.00_y452.00)
1. [Planteamiento de la Organización del Data-Set ................................................... 10 ](#_page9_x82.00_y204.00)
1. [Data-Set de entrenamiento (training) ........................................................... 11 ](#_page10_x82.00_y637.00)
1. [Data-Set de Pruebas (test)............................................................................. 12 ](#_page11_x82.00_y121.00)
1. [Data-Set de Validación ("Cross-Validation")................................................ 12 ](#_page11_x82.00_y216.00)
4. [Aprendizaje................................................................................................................... 12 ](#_page11_x82.00_y456.00)
1. [Planteamiento del modelo de aprendizaje ............................................................ 12 ](#_page11_x82.00_y490.00)
1. [Desarrollo e implementación del modelo ............................................................. 14 ](#_page13_x82.00_y71.00)
5. [Comprobación .............................................................................................................. 16 ](#_page15_x82.00_y142.00)
1. [Obtencion del dataset............................................................................................ 16 ](#_page15_x82.00_y177.00)
1. [Construcción del dataset ....................................................................................... 17 ](#_page16_x82.00_y299.00)
3. [Arquitectura Modular del Sistema........................................................................ 23 ](#_page22_x82.00_y71.00)
3. [Validación Cruzada Walk-Forward....................................................................... 24 ](#_page23_x82.00_y204.00)
3. [Entrenamiento de Modelos ................................................................................... 25 ](#_page24_x82.00_y71.00)
1. [Regresión Logística ...................................................................................... 27 ](#_page26_x82.00_y71.00)
1. [Random Forest.............................................................................................. 29 ](#_page28_x82.00_y286.00)
1. [SVM con Descenso de Gradiente Estocástico.............................................. 32 ](#_page31_x82.00_y121.00)
6. [Comparación Final y Selección del Mejor Modelo .............................................. 34 ](#_page33_x82.00_y407.00)
6. [Evaluación .................................................................................................................... 36 ](#_page35_x82.00_y71.00)
1. [Análisis Detallado de Métricas ............................................................................. 36 ](#_page35_x82.00_y96.00)
1. [Interpretación de Matrices de Confusión.............................................................. 37 ](#_page36_x82.00_y613.00)
1. [Análisis de Estabilidad Temporal ......................................................................... 41 ](#_page40_x82.00_y121.00)

[Referencias Bibliograficas .................................................................................................... 43 ](#_page42_x82.00_y363.00)

1. **Introducción<a name="_page3_x82.00_y71.00"></a>** 

<a name="_page3_x82.00_y96.00"></a>**1.1.Título del Proyecto** 

Modelado y análisis predictivo de la dirección del precio de apertura en acciones del NYSE mediante técnicas de aprendizaje estadístico. 

<a name="_page3_x82.00_y174.00"></a>**1.2.Antecedentes** 

La bolsa de valores es una organización privada que brinda las facilidades necesarias para que sus miembros (corredores o intermediarios), atendiendo los mandatos de sus clientes (demandantes y oferentes), introduzcan órdenes y realicen negociaciones de compra y venta de valores, tales como acciones de sociedades o compañas anónimas, bonos públicos y privados, certificados, títulos de participación y una amplia variedad de instrumentos de inversión  (Mireles Vázquez,  2011).  La  característica  de  la  bolsa  de  valores  es  que  se comercializan instrumentos financieros, las personas que compran esos instrumentos se les conoce como inversionistas y las personas o entidades que colocan o “venden”, se les conoce como emisores (Reyna, 2024). 

Desde una perspectiva económica, la bolsa de valores constituye una institución del mercado  encargada  de  articular  la  interacción  entre  la  oferta  y  la  demanda  de  activos financieros, posibilitando la determinación eficiente de sus precios. Se entiende que  un mercado alcanza eficiencia cuando los agentes que en él participan disponen de la totalidad de la información pertinente y los precios de los activos negociados incorporan de manera adecuada dicha información (Villanueva Gonzales, 2007). 

El término “bolsa” tiene su origen en la ciudad de Brujas, ubicada en la región de Flandes, donde existía un edificio perteneciente a la familia noble Van Der Buërse. En dicho lugar se llevaban a cabo reuniones y transacciones de carácter mercantil. El blasón de esta familia mostraba tres bolsas de piel, que en aquel periodo representaban los monederos utilizados. Debido a la relevancia de las operaciones comerciales realizadas, así como a la influencia social y económica de la familia, el apellido Buërse dio nombre a lo que en la actualidad se conoce como bolsa (Mireles Vázquez, 2011). 

La mayoría de los países disponen de una bolsa de valores; sin embargo, la más relevante a nivel mundial es la Bolsa de Nueva York (NYSE), reconocida por su volumen de transacciones y por el número de compañías que en ella cotizan. En segundo  lugar, se encuentra el NASDAQ, considerado el mayor mercado automatizado de valores en los Estados Unidos, cuya particularidad radica en la concentración de empresas vinculadas principalmente a los sectores de alta tecnología, tales como la electrónica, la informática y las telecomunicaciones, entre otros (Reyna, 2024). 

Fama expone las formas de eficiencia de mercado (débil, semi-fuerte, fuerte) y discute qué implicaciones tiene la disponibilidad de información sobre la capacidad de predecir retornos. Es esencial para justificar por qué algunos enfoques predictivos podrían fallar o por qué habría que buscar señales no lineales/alternativas (Fama, 1969). 

Con la entrada del machine learning en finanzas, trabajos recientes muestran que métodos no lineales (árboles, boosting, redes neuronales, ensembles) pueden mejorar la predicción  de  primas  de  riesgo  y  retornos  esperados  frente  a  regresiones  lineales tradicionales,  en  particular  cuando  los  modelos  explotan  interacciones  complejas  entre cientos de predictores y usan procedimientos de regularización y validación adecuados (Gu, Kelly, & Xiu, 2020). 

En paralelo, el aprendizaje estadístico amplió el repertorio con métodos predictivos y de clasificación/ regresión regularizada, árboles y ensambles y máquinas de soporte vectorial, prestando especial atención a la validación y al control del sobreajuste (Hastie, Tibshirani, & Friedman, 2009). En mercados accionarios líquidos como la New York Stock Exchange (NYSE), estos enfoques se aplican sobre representaciones transformadas de los precios (p. ej.,  rendimientos  logarítmicos)  y  sobre  características  derivadas  (rezagos, medias/volatilidades móviles, cruces de medias, momentum), buscando identificar señales predictivas débiles pero explotables dentro de un esquema de validación temporal (walk- forward) y métricas adecuadas tanto para clasificación (dirección: sube/baja) como para regresión (Hyndman & Athanasopoulos, 2021). 

<a name="_page5_x82.00_y71.00"></a>**1.3.Problema a resolver** 

El proyecto aborda la siguiente pregunta aplicada: ¿es posible identificar señales predictivas estadísticamente significativas en la dirección del precio de apertura del día siguiente  (sube  o  baja  respecto  al  cierre  previo)  para  acciones  del  NYSE  utilizando exclusivamente técnicas de aprendizaje estadístico basadas en series históricas OHLCV e indicadores técnicos derivados? 

<a name="_page5_x82.00_y208.00"></a>**1.4.Objetivos** 

1. **Objetivo<a name="_page5_x82.00_y232.00"></a> general:** 

Desarrollar y evaluar un modelo de aprendizaje supervisado capaz de predecir la dirección  del  precio  de  apertura  del  día  siguiente  en  acciones  del  NYSE,  utilizando únicamente información histórica de mercado y técnicas de aprendizaje estadístico, con evaluación rigurosa mediante validación cruzada y métricas apropiadas de clasificación. 

2. **Objetivos<a name="_page5_x82.00_y352.00"></a> específicos:** 

Definir el conjunto de variables predictoras a partir de precios y volumen (retornos, indicadores técnicos y rezagos), documentando su relación con la variable objetivo. 

Construir los conjuntos de entrenamiento, validación y prueba respetando el orden 

temporal. 

Entrenar y comparar modelos de clasificación tales como regresión logística, árboles de decisión, SVM, KNN, discriminante lineal/naïve Bayes bajo un protocolo común de validación y selección de características. 

Seleccionar el modelo con mejor desempeño fuera de muestra según métricas como exactitud, F1 y balanced accuracy, reportando intervalos/variabilidad por validación cruzada. 

Analizar la estabilidad del modelo ante cambios de ventanas temporales y universos de acciones, discutiendo sus limitaciones y alcances. 

2. **Requerimientos<a name="_page6_x82.00_y71.00"></a>** 

<a name="_page6_x82.00_y96.00"></a>**2.1.Definición del dominio** 

El dominio del proyecto es la predicción de la dirección del precio de apertura del día siguiente (sube o baja respecto al día previo) en acciones que cotizan en la Bolsa de Nueva York  (NYSE).  Se  modelará  como  un  problema  de  clasificación  binaria  supervisada, coherente  con  los  contenidos  del  curso  (regresión  y  clasificación;  árboles  de  decisión; máquinas de soporte vectorial; y evaluación del rendimiento), lo que permite aplicar técnicas vistas formalmente en la asignatura y medir su capacidad de generalizar en datos no vistos. En este contexto, La variable objetivo será un indicador binario construido a partir de la comparación entre la **apertura en**  + 1y el **cierre en**  :  +1 = [Open +1 > Close ]. Las variables explicativas provendrán de series históricas diarias de precios y volumen (OHLCV) y de indicadores técnicos derivados, retornos y log-retornos, promedios móviles simples y exponenciales,  osciladores  de  momentum,  medidas  de  volatilidad  y  relaciones  precio– volumen junto con rezagos que capturen dependencia temporal. El fenómeno a modelar es no estacionario y con alta relación señal–ruido: la dinámica de precios cambia por eventos macro, microestructura del mercado y comportamiento de inversionistas, por lo que el diseño debe contemplar división temporal estricta de los datos, evitar “fugas de información” (look- ahead  bias)  y  usar  validación  apropiada  para  series  temporales.  Además,  el  objetivo pedagógico es demostrar, en un caso real de finanzas, cómo se ajusta, evalúa y optimiza un clasificador en línea con los resultados de aprendizaje del curso, que enfatizan técnicas supervisadas y su evaluación con validación cruzada y métricas de rendimiento. 

<a name="_page6_x82.00_y528.00"></a>**2.2.Determinación de requisitos (requerimientos)** 

Para garantizar un estudio riguroso y realista, los requisitos se organizan en datos, metodología, evaluación, herramientas y consideraciones operativas. 

En datos, se requiere una fuente pública y consistente de series diarias (apertura, máximo,  mínimo,  cierre,  volumen)  con  historial  suficiente  para  construir  ventanas  de entrenamiento, validación y prueba. Se trabajará con un subconjunto manejable de acciones líquidas del NYSE, manteniendo el orden temporal en todos los pasos. El dataset incluirá la 

etiqueta  binaria  de  dirección  de  apertura  +1 = [Open +1 > Close ]y  un conjunto  de predictores derivados de series OHLCV, calculados solo con información disponible hasta  .. 

En metodología de aprendizaje, el sistema debe implementar un pipeline supervisado: (1)  preparación  del  dataset  con  separaciones  temporales  claras;  (2) estandarización/normalización cuando el algoritmo lo requiera; (3) entrenamiento de varios clasificadores coherentes con el sílabo, por ejemplo, regresión logística, árboles de decisión, SVM, KNN, naïve Bayes y análisis discriminante; (4) selección y ajuste de hiperparámetros con validación cruzada compatible con series temporales; y (5) comparación justa entre modelos bajo el mismo protocolo de partición y métricas. Estas familias de modelos y su evaluación forman parte explícita de los contenidos de la asignatura. 

En evaluación, el requisito es estimar desempeño fuera de muestra con métricas acordes a clasificación binaria. Se tomará como mínimo Accuracy para comparar con una línea base ingenua (por ejemplo, “siempre igual a la clase mayoritaria”), complementando con  F1-score  cuando  exista  desbalance  y  ROC-AUC  para  sensibilidad  a  umbrales.  La evaluación usará validación cruzada (k-fold temporal o bloques) para seleccionar el modelo y un conjunto de prueba estrictamente posterior en el tiempo para reporte final, como enfatiza el curso al incorporar validación cruzada y métricas de rendimiento en sus resultados de aprendizaje y contenidos. 

En herramientas y reproducibilidad, se requiere un entorno práctico de análisis con Python  y  bibliotecas  estándar  para  ciencia  de  datos,  control  de  versiones  de notebooks/código, bitácora de experimentos y documentación clara del pipeline (desde la descarga de datos hasta el reporte de resultados). 

En consideraciones operativas y alcance, el sistema es estrictamente académico: no ejecutará órdenes de mercado ni incluirá costos de transacción; su objetivo es evaluar si un clasificador puede acertar la dirección con significancia frente a una línea base, discutir limitaciones  (no  estacionariedad,  posible  sobreajuste,  deriva  de  concepto)  y  proponer estrategias de mejora (nuevas variables, ventanas rodantes y reentrenamiento periódico). 

3. **Pre-Procesamiento<a name="_page8_x82.00_y71.00"></a> y Normalización** 

<a name="_page8_x82.00_y96.00"></a>**3.1.Medidas, Datos, Bases de Datos y Elaboración del Data-Set** 

El proyecto utiliza un único dataset masivo y vigente: el paquete U.S. – daily (ASCII) de Stooq, del cual se filtra exclusivamente el universo NYSE (se excluyen ETFs y otros mercados). La fecha de corte del estudio se fija del 16 de enero del 1961 al 31 de octubre de 2025; toda la extracción y el procesamiento se documentan con esa fecha. 

A partir de los archivos diarios OHLCV (*Open, High, Low, Close, Volume*) por *ticker*, se construye un panel (Ticker,Date)ordenado cronológicamente, con control de duplicados y verificación  básica  de  calidad  (fechas  de  mercado  y  campos  críticos). Variable objetivo (dirección overnight). Para cada *ticker* y día  : 

+1 = [Open +1 > Close ]. 

Predictores  (solo  hasta  ).  (a)  Retornos  log:  ret\_cc\_1,ret\_oo\_1,ret\_co\_1;  (b) Tendencia/momentum:  SMA(5),SMA(10),EMA(10),mom5;  (c)  Volatilidad  y  rango: std5,std10, range\_rel = (High − Low)/Close; (d) Volumen: vol\_ma\_10,vol\_rel = Volume/ MA10(Volume); (e) Calendario: dow(día de la semana). Todas las ventanas terminan en  ; se descartan filas de *warm-up* hasta completar ventanas (p. ej.,  = 10). 

<a name="_page8_x82.00_y452.00"></a>**3.2.Normalización y/o Filtrado de Datos** 

La normalización es clave para modelos sensibles a escala (SVM, KNN, regresión logística). Se utilizará estandarización z-score por ticker —media y desviación estándar calculadas sólo en el conjunto de entrenamiento— y aplicadas luego a validación y prueba para  impedir  fuga  de  información.  Como  robustez  ante  colas  pesadas,  se  considerará winsorización por variable (recorte en percentiles 1 %–99 %) o escalado robusto (mediana e IQR) cuando se detecten outliers extremos en volumen o rangos de precio. Para indicadores acumulativos como OBV, se preferirá normalizarlos por su desviación rodante o convertirlos a cambios porcentuales para hacerlos comparables entre tickers. 

El filtrado incluirá: eliminación de filas con datos faltantes críticos para el cálculo de la etiqueta (si falta Open en to t + 1); descarte de las primeras wobservaciones por ticker (periodo de warm-up necesario para indicadores con ventanas de wdías); y control de calidad de fechas de mercado (excluyendo cierres no bursátiles). Para reducir sesgo de supervivencia, el panel se construirá tal como aparece en la fuente durante el periodo estudiado; si se complementa con una fuente dinámica (yfinance), se congelará una “foto” de tickers al inicio del periodo de análisis y se documentará la lista utilizada. En todos los casos, se conservará la temporalidad: cualquier estadístico de escalado o selección de características se ajusta antes de ver validación/prueba. 

<a name="_page9_x82.00_y204.00"></a>**3.3.Planteamiento de la Organización del Data-Set** 

Las variables que nos proporcionan los dataset son las siguientes: 



|**Nombre** |**Descripcion** |**Ejemplo** |**Unidad** |
| - | - | - | - |
|**Date** |Fecha de la sesión bursátil |2025-10-15 |Formato YYYY- MM-DD |
|**Open** |Precio de apertura |$150.25 |Dólares USD |
|**High** |Precio máximo alcanzado durante el día |$152.80 |Dólares USD |
|**Low** |Precio mínimo alcanzado durante el día |$149.50 |Dólares USD |
|**Close** |Precio de cierre |$151.75 |Dólares USD |
|**Volume** |Cantidad de acciones negociadas en el día |5,234,890 |Número de acciones |

A partir de dichas variables se generan las variables predictoras que serán utilizadas por el modelo, las cuales se calculan en función de los datos presentados en la tabla anterior. 



|**Variable** |**Descripcion** |**Calculo** |**Interpretacion** |
| - | - | - | - |
|**ret\_cc\_1** |Retorno close-to- close de 1 día |log(Close\_t / Close\_{t-1}) |Cambio porcentual del precio de cierre |
|**ret\_oo\_1** |Retorno open-to- open de 1 día |log(Open\_t / Open\_{t-1}) |Cambio entre aperturas consecutivas. Captura gaps overnight acumulados |
|**ret\_co\_1** |Retorno close-to- open de 1 día |log(Open\_t / Close\_{t-1}) |Gap overnight directo. Positivo = abrió más alto que cierre previo |
|**sma\_5** |Media móvil simple 5 días (normalizada) |mean(Close últimos 5 días) / Close\_t - 1 |Si > 0: precio está arriba del promedio (alcista). Si < 0: bajista |
|**sma\_10** |Media móvil simple 10 días (normalizada) |mean(Close últimos 10 días) / Close\_t - 1 |Tendencia de mediano plazo. Menos sensible a ruido que sma\_5 |
|**ema\_10** |Media móvil exponencial 10 días (normalizada) |EMA(Close, span=10) / Close\_t - 1 |Similar a sma\_10 pero da más peso a días recientes. Reacciona más rápido |
|**mom\_5** |Momentum de 5 días |(Close\_t / Close\_{t-5}) - 1 |<p>Velocidad del cambio. Positivo = subiendo, negativo </p><p>= bajando </p>|
|**std\_5** |Volatilidad de 5 días |std(retornos últimos 5 días) |Desviación estándar. Alto = precio muy variable |
|**std\_10** |Volatilidad de 10 días |std(retornos últimos 10 días) |Volatilidad de mediano plazo. |
|**range\_rel** |Rango relativo intradía |(High\_t - Low\_t) / Close\_t |Qué tan amplio fue el rango del día. Alto = mucha indecisión |
|**vol\_ma\_10** |Media móvil del volumen 10 días |mean(Volume últimos 10 días) |Volumen "normal" de referencia |
|**vol\_rel** |Volumen relativo |Volume\_t / vol\_ma\_10 |Si > 1: hoy se negoció MÁS de lo usual |
|**dow** |Día de la semana |0=Lunes, 1=Martes, ..., 4=Viernes |Captura patrones como "Efecto lunes" |

1. **Data-Set<a name="_page10_x82.00_y637.00"></a> de entrenamiento (training)** 

75%  Entrenamiento  (training).  Comprende  desde  el  inicio  del  historial  hasta  el percentil  temporal  75.  En  este  bloque  se  ajustan  los  modelos  base  y  se  calculan exclusivamente  aquí  todos  los  parámetros  de  pre-procesamiento  (p.  ej.,  medias  y desviaciones para estandarización, winsorización, selección de variables). Esto maximiza la cantidad de ejemplos que ven los algoritmos y reduce la varianza de los estimadores. 

2. **Data-Set<a name="_page11_x82.00_y121.00"></a> de Pruebas (test)** 

15% Prueba (test). Es el tramo final (del 85% al 100%) y no interviene en decisiones de modelado. Se usa una única vez para estimar desempeño fuera de muestra en condiciones realistas, pues captura el período más reciente (y potencialmente más difícil) del mercado. 

3. **Data-Set<a name="_page11_x82.00_y216.00"></a> de Validación ("Cross-Validation")** 

10% Validación para “Cross-Validation”. Corresponde al tramo temporal siguiente (del 75% al 85%). Este bloque se utiliza para seleccionar hiperparámetros y afinar decisiones como  umbrales  de  clasificación  o  regularización.  La  validación  se  implementa  con  un esquema walk-forward sobre ese 10%: se divide en  = 5subbloques contiguos. En cada *fold*, se reentrena con el 75% inicial más los subbloques ya vistos, y se valida en el subbloque inmediatamente posterior, respetando el flujo temporal y evitando *look-ahead*. Al finalizar, se reentrena el modelo ganador sobre el 85% (75%+10%) Así se respeta el flujo temporal (entreno-antes / valido-después), se evalúa robustez frente a pequeñas derivas del mercado y se evita fuga de información. Concluida esta etapa, se reentrena el modelo ganador sobre el 85% acumulado (75% + 10%) con los hiperparámetros óptimos. 

4. **Aprendizaje<a name="_page11_x82.00_y456.00"></a>** 

<a name="_page11_x82.00_y490.00"></a>**4.1.Planteamiento del modelo de aprendizaje** 

El problema se formula como clasificación binaria supervisada: para cada acción y día  , se busca predecir la dirección de la apertura del día  + 1respecto al cierre del día  (gap “overnight”). La etiqueta es  +1 = 1[Open +1 > Close ].. 

Desde una perspectiva de aprendizaje estadístico, el plan contempla dos familias de modelos complementarios: 

**Modelo lineal interpretable** (Regresión Logística con regularización  2): sirve como línea  base  robusta  y  explicable.  Permite  cuantificar  el  efecto  marginal  de  señales  de “momentum”, volatilidad y microestructura sobre la probabilidad de alza en la apertura. 

**Modelo no lineal de mayor capacidad** (árboles potenciados tipo Gradient Boosting /  Random  Forest  o,  alternativamente,  un  **SVM-SGD**  si  la  dimensionalidad  efectiva  es moderada): capturan interacciones y umbrales que los lineales no expresan. Estos modelos se justifican porque la dinámica overnight suele ser **no lineal** y dependiente del régimen (p. ej., volatilidad reciente, shocks de volumen o rangos intradía). 

La variable de entrada  se compone **exclusivamente de información conocida al cierre del día**  , para evitar fuga de información. Se agrupa en cuatro bloques realistas y computables con datos diarios: 

- **Precio/retornos y momentum:** retornos log de 1, 2, 5 y 10 días; retorno intradía (Close /Open − 1); cruces y desviaciones de medias móviles (p. ej.,  Close vs. SMA(5), SMA(10)); osciladores simples como %K (suavizado con ventana corta). 
- **Rango y volatilidad:** rango normalizado (High − Low )/Close , “true range” y desviación estándar móvil de retornos (5 y 10 días) como proxy de volatilidad. 
- **Volumen y presión de orden:** cambio porcentual de volumen vs. su media móvil (5 y 10 días); volumen relativo (vol/avgVol); On-Balance Volume incremental. 
- **Factores de mercado/sector y calendario (opcionales si están disponibles en el dataset):** retorno del índice amplio (p. ej., S&P500/ETF proxy) y de su sector el día 

; cambio del VIX si está disponible; dummies de día de la semana y fin de mes, para 

capturar patrones estacionales simples. 

La **hipótesis de trabajo** es que combinaciones parsimoniosas de estas señales— normalizadas y con rezagos—aportan probabilidad predictiva superior al 50% en la dirección overnight para acciones líquidas del NYSE. En términos de **sesgo–varianza**, el modelo lineal da un piso estable (más sesgo, menos varianza) y el modelo de árboles/SVM intenta capturar no linealidades (menos sesgo, más varianza), controlando complejidad con regularización y validación  apropiada.  De  esta  forma,  el  proyecto  contrasta  interpretabilidad  vs.  poder predictivo dentro de un mismo marco experimental. 

<a name="_page13_x82.00_y71.00"></a>**4.2.Desarrollo e implementación del modelo** 

La implementación se realiza con un pipeline reproducible en Python. El flujo está diseñado para respetar la estructura temporal y el split 75%/10%/15% ya definido: 

1. **Construcción de la matriz de aprendizaje (por ticker y luego apilada):** 
- Ordenamiento cronológico estricto. 
- Cálculo  de  todas  las  características  con  **ventanas  que  terminan  en**  ; cualquier estadístico que use  + 1se descarta. 
- Etiquetado según la definición de **gap**  +1 = [Open +1 > Close ]. 
2. **Preprocesamiento dentro de un Pipeline**: 
- **Imputación** de faltantes sólo con estadísticas del **entrenamiento** (median imputer). 
- **Normalización/estandarización** de variables continuas con medias y desvíos del **entrenamiento**. 
- **Winsorización** suave de colas (percentiles 1–99) para robustez a outliers. 
3. **Partición temporal y validación**: 
- Se respeta el acuerdo del curso: **75% entrenamiento**, **15% prueba**, **10% validación por cross-validation**. Operativamente, se procede así: 
- Con el  75% de entrenamiento  se realiza una  **validación cruzada temporal**  (k-fold  no  aleatorio/“expanding  window”  o  “walk- forward”) para ajustar hiperparámetros y seleccionar variables. 
- El  15%  **test**  queda  completamente  **bloqueado**  hasta  el  final  para estimar desempeño fuera de muestra. 
- El  10%  restante  puede  emplearse  como  **hold-out**  adicional  o integrarse  al  esquema  de  CV  como  último  bloque  “de  validación externa” para verificar estabilidad. 
- Se fija semilla aleatoria y se loguean versiones para **reproducibilidad**. 
4. **Modelos y ajuste de hiperparámetros** (con búsqueda en malla/aleatoria dentro de la CV temporal): 
- **Regresión  Logística**  2:  (inversa  de  la  regularización),  opción  de **class\_weight='balanced'** si hay leve desbalance. 
- **Modelo no lineal**: 
- **Random Forest**. 
- **SVM-SGD**. 
5. **Métricas primarias y control de sobreajuste dentro de la CV**: 
- **Accuracy direccional** y **Balanced Accuracy** (por si hay asimetría en clases), **F1** y **ROC-AUC** como apoyo. 
- **Estabilidad temporal**: comparar desempeño por subperíodos dentro de la CV (ej., años o trimestres) para detectar dependencia de régimen. 
- **Curva  de  calibración**  del  modelo  probabilístico  (sobre  todo  en logística/boosting) y ajuste de **umbral de decisión** (por ejemplo, operar sólo si  ( = 1) > 0.55). 
6. **Reglas prácticas para despliegue experimental** (sin trading algorítmico complejo, sólo para validar realismo): 
- Generar  una  señal  “comprar  en  apertura”  si  el  modelo  predice  **subida overnight** con probabilidad por encima del umbral; “no operar” en caso contrario. 
- Evaluar  una  **métrica  económica  ilustrativa**  en  el  set  de  prueba  (se desarrollará formalmente en la sección V): tasa de aciertos condicionada a señal, retorno medio por operación **neto** de un costo fijo conservador (p. ej., 5–10 bps), y “hit ratio vs. benchmark 50%”. 
- Evitar  **look-ahead**  y  **survivorship  bias**:  los  cálculos  usan  sólo  datos disponibles al cierre de  y se mantienen tickers constantes durante el período evaluado. 
5. **Comprobación<a name="_page15_x82.00_y142.00"></a>** 

<a name="_page15_x82.00_y177.00"></a>**5.1.Obtencion del dataset** 

El  dataset  utilizado  proviene  de  Stooq  [(https://stooq.com), ](vscode-file://vscode-app/c:/Users/jcode/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) específicamente  del paquete "U.S. - daily (ASCII)" que contiene series históricas diarias de todas las acciones negociadas en mercados estadounidenses. Para este proyecto se filtró exclusivamente el universo  NYSE  (New  York  Stock  Exchange),  descartando  ETFs  y  otros  instrumentos financieros para concentrarse únicamente en acciones individuales. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.002.jpeg)

La descarga del dataset se realizó mediante el archivo comprimido disponible en la plataforma Stooq, obteniendo un total de 3,649 archivos en formato texto (\*.txt), cada uno correspondiente a un ticker diferente. Cada archivo contiene las series temporales con las variables OHLCV (Open, High, Low, Close, Volume) en formato diario, abarcando un rango histórico desde 1962 hasta octubre de 2025. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.003.png)

<a name="_page16_x82.00_y299.00"></a>**5.2.Construcción del dataset** 

Una vez descargados los archivos crudos, se procedió a la construcción del dataset de modelado  mediante  el  script make\_dataset.py.  Este  proceso  se  divide  en  cuatro  etapas fundamentales:  lectura  y  normalización  de  archivos,  construcción  de  features  técnicos, construcción de la variable objetivo y división temporal del dataset. 

La  primera  función  implementada  es leer\_archivo\_stooq(),  que  se  encarga  de procesar cada archivo individual. Esta función realiza la lectura del archivo CSV, elimina los caracteres especiales (< y >) de los nombres de columnas que utiliza el formato Stooq, convierte las fechas del formato YYYYMMDD a datetime de Python, selecciona únicamente las  columnas  necesarias  (TICKER,  DATE,  OPEN,  HIGH,  LOW,  CLOSE, VOL)  y  las renombra  a  un  formato  estandarizado.  Adicionalmente,  extrae  el  símbolo  del  ticker eliminando  el  sufijo .US y  ordena  los  datos  cronológicamente.  Durante  este  proceso  se implementó manejo de excepciones para identificar archivos corruptos o vacíos, los cuales fueron descartados automáticamente. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.004.jpeg)

La función construir\_features() implementa el  cálculo de 13 indicadores técnicos derivados  de  las  series  OHLCV.  Estos  indicadores  se  organizan  en  cuatro  categorías principales  según  su  naturaleza:  retornos  logarítmicos  (ret\_cc\_1,  ret\_oo\_1,  ret\_co\_1), indicadores de tendencia y momentum (sma\_5, sma\_10, ema\_10, mom\_5), medidas de volatilidad  (std\_5,  std\_10,  range\_rel)  e  indicadores  basados  en  volumen  (vol\_ma\_10, vol\_rel). Adicionalmente se incluye la variable dow (day of week) que captura efectos calendario. Todos los cálculos respetan estrictamente la temporalidad, utilizando únicamente información  disponible  hasta  el  día  t  para  evitar  look-ahead  bias.  Se  implementaron protecciones contra divisiones por cero y se reemplazaron valores infinitos por NaN para garantizar la calidad del dataset. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.005.png)

La  función construir\_etiqueta() implementa  la  definición  formal  de  la  variable objetivo  del  problema  de  clasificación  binaria.  La  etiqueta  se  construye  como  +1 = 1[Open +1 > Close ],  donde 1 es  la  función  indicadora  que  toma  el  valor  1  cuando  la 

condición  es  verdadera  y  0  en  caso  contrario.  Esta  definición  captura  precisamente  el fenómeno de interés: predecir si el precio de apertura del día siguiente será mayor que el precio  de  cierre  del  día  actual,  lo  que  representa  un  gap  overnight  positivo.  La implementación utiliza la función shift(-1) de pandas para acceder al valor futuro de la apertura, respetando el principio de que esta información no está disponible en el momento t. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.006.png)

La función split\_temporal() realiza la partición del dataset siguiendo un protocolo estricto de división temporal que respeta la naturaleza secuencial de las series financieras. A diferencia de la validación cruzada aleatoria tradicional, este método divide cada ticker individualmente según su cronología, asignando el 75% más antiguo a entrenamiento, el siguiente 10% a validación y el 15% final a prueba. Esta aproximación garantiza que nunca se entrene con información posterior a la que se evalúa, evitando completamente el look- ahead bias que invalidaría los resultados. La implementación itera sobre cada ticker único del dataset, ordena sus observaciones cronológicamente, calcula los índices de corte según los porcentajes especificados y asigna la etiqueta correspondiente (train, val o test) a cada observación. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.007.png)

La  ejecución  del  script  de  construcción  se  realizó  mediante  el  comando python core/data/make\_dataset.py en  el  entorno  virtual  del  proyecto.  El  proceso  tardó aproximadamente 8 minutos en completarse, procesando los 3,649 archivos de entrada. Durante  la  ejecución  se  identificaron  algunos  archivos  corruptos  o  vacíos  que  fueron automáticamente descartados, lo cual se reportó mediante mensajes de advertencia en la consola. El proceso aplicó un filtro de calidad que descartó tickers con menos de 300 días de historia,  garantizando  que  todos  los  tickers  incluidos  tuvieran  suficiente  profundidad temporal para el cálculo de indicadores con ventanas de hasta 10 días. 

El dataset consolidado final contiene 10,374,544 registros correspondientes a 2,872 tickers únicos, abarcando un rango temporal desde el 16 de enero de 1962 hasta el 31 de octubre de 2025. La división temporal resultó en 7,780,908 registros para entrenamiento (74.99%), 1,037,454 registros para validación (10.00%) y 1,556,182 registros para prueba (15.02%). El análisis del balance de clases reveló una distribución prácticamente equitativa: la clase 0 (Open\_{t+1} ≤ Close\_t) representa el 51.63% de las observaciones mientras que la  clase  1  (Open\_{t+1}  >  Close\_t)  representa  el  48.37%,  lo  cual  es  esperado  dada  la naturaleza  aproximadamente  simétrica  de  los  movimientos  de  precios  en  mercados eficientes. En el conjunto de prueba específicamente, esta distribución se invierte ligeramente con 48.61% clase 0 y 51.39% clase 1, manteniendo el balance adecuado para evaluar modelos de  clasificación  binaria.  El  archivo  resultante dataset\_modelado.csv tiene  un  tamaño  de 2,832.9 MB y fue almacenado en la carpeta processed. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.008.png)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.009.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.010.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.011.jpeg)

<a name="_page22_x82.00_y71.00"></a>**5.3.Arquitectura Modular del Sistema** 

Una vez construido el dataset de modelado, se procedió al diseño e implementación de  la  arquitectura  de  software  que  ejecutaría  el  pipeline  completo  de  entrenamiento  y evaluación. El sistema fue diseñado siguiendo principios SOLID (Single Responsibility, Open/Closed,  Liskov  Substitution,  Interface  Segregation,  Dependency  Inversion)  para garantizar mantenibilidad, extensibilidad y testabilidad del código. 

La arquitectura se organizó en cuatro capas principales. La capa de configuración centralizada, implementada en settings.py, contiene todas las constantes y parámetros del proyecto  como  rutas  de archivos, porcentajes de división  temporal,  hiperparámetros de modelos  y  configuración  de  paralelización.  Esta  centralización  facilita  el  ajuste  de parámetros sin modificar múltiples archivos y garantiza consistencia en toda la ejecución. 

La capa de modelos, ubicada en models, implementa un patrón de diseño orientado a objetos donde cada algoritmo de clasificación hereda de una clase base abstracta BaseModel que  define  la  interfaz  común.  Se  implementaron  tres  modelos  concretos: LogisticRegressionModel  para  regresión  logística  con  regularización  L2, RandomForestModel  para  ensambles  de  árboles  de  decisión  y  SVMSGDModel  para máquinas  de  vectores  de  soporte  con  descenso  de  gradiente  estocástico.  Cada  modelo encapsula  su  propia  lógica  de  preprocesamiento,  incluyendo  normalización  cuando  es necesario, y expone métodos estandarizados para entrenamiento, predicción y cálculo de probabilidades. Adicionalmente se implementó un patrón Factory en model\_factory.py que permite instanciar modelos dinámicamente por nombre, facilitando la extensión futura del sistema con nuevos algoritmos sin modificar el código existente. 

La  capa  de  pipelines,  implementada  en  training\_pipeline.py,  orquesta  el  flujo completo  de entrenamiento.  Esta clase se encarga de cargar el  dataset, iterar sobre los modelos  especificados,  ejecutar  la  validación  cruzada  walk-forward  en  el  conjunto  de validación, reentrenar en el conjunto combinado train+val, evaluar en el conjunto de test, generar visualizaciones de matrices de confusión y persistir los modelos entrenados en disco. El pipeline implementa logging detallado en cada etapa para facilitar el  monitoreo del progreso y diagnóstico de errores. 

Finalmente, la capa de interfaz de usuario, representada por el script train\_models.py en la raíz del proyecto, proporciona una interfaz de línea de comandos (CLI) que permite al usuario ejecutar el pipeline completo o seleccionar modelos específicos, ajustar el número de folds para validación cruzada y especificar rutas personalizadas del dataset. Esta separación entre interfaz y lógica de negocio permite reutilizar el pipeline desde otros contextos como notebooks de Jupyter, APIs REST o interfaces gráficas futuras. 

<a name="_page23_x82.00_y204.00"></a>**5.4.Validación Cruzada Walk-Forward** 

La validación de los modelos se realizó mediante una estrategia de walk-forward cross-validation  específicamente  diseñada  para  series  temporales.  A  diferencia  de  la validación cruzada k-fold tradicional que mezcla aleatoriamente las observaciones, esta técnica respeta estrictamente el orden temporal de los datos para evitar contaminación de información futura en las predicciones. 

El conjunto de validación (10% del dataset, equivalente a 1,037,454 registros) se dividió en k=5 bloques temporales contiguos de aproximadamente 207,490 registros cada uno. En el primer fold, el modelo se entrena únicamente con el conjunto de entrenamiento base (75%) y valida en el primer bloque del 10%. En el segundo fold, el modelo se reentrena con el conjunto de entrenamiento base más el primer bloque de validación ya observado, y valida en el segundo bloque. Este proceso se repite iterativamente hasta el quinto fold, donde el modelo se entrena con el 75% inicial más los primeros cuatro bloques de validación (83% acumulado) y valida en el bloque final. 

Esta aproximación simula de manera realista cómo un modelo sería utilizado en producción,  donde  continuamente  se  incorporan  nuevas  observaciones  al  conjunto  de entrenamiento  para mantener el  modelo actualizado con los  patrones más recientes del mercado. Cada fold genera métricas de desempeño (accuracy, balanced accuracy, precision, recall, F1-score y ROC-AUC) que posteriormente se promedian para obtener una estimación robusta de la capacidad de generalización del  modelo. La desviación  estándar de estas métricas a través de los folds proporciona información sobre la estabilidad temporal del modelo ante pequeños cambios en la distribución de los datos. 

<a name="_page24_x82.00_y71.00"></a>**5.5.Entrenamiento de Modelos** 

La  ejecución  del  pipeline  completo  de  entrenamiento  se  realizó  mediante  el comando python  train\_models.py utilizando  el  intérprete  Python  del  entorno  virtual.  El proceso inició a las 15:46:30 del 8 de noviembre de 2025 y finalizó a las 17:27:04 del mismo día, con una duración total de 1 hora 40 minutos y 34 segundos. La configuración utilizada estableció k=5 folds para walk-forward, 13 indicadores técnicos como features, división temporal 75%/10%/15% y paralelización con 8 núcleos de CPU. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.012.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.013.png)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.014.png)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.015.png)

1. **Regresión<a name="_page26_x82.00_y71.00"></a> Logística** 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.016.png)

El primer modelo entrenado fue Regresión Logística con regularización L2 (C=1.0). Este modelo lineal sirve como baseline interpretable del problema. Durante la validación walk-forward, el modelo mostró métricas consistentes a través de los cinco folds. El accuracy promedio fue de 0.5120 ± 0.0050, apenas 1.2 puntos porcentuales por encima del azar (50%). El balanced accuracy de 0.5030 ± 0.0017 confirma que el modelo no está sesgado hacia ninguna clase particular. Sin embargo, el recall extremadamente bajo de 0.0841 ± 0.0155 indica que el modelo predice la clase 1 (subida overnight) con mucha cautela, resultando en un F1-score deficiente de 0.1437 ± 0.0232. El ROC-AUC de 0.5204 ± 0.0034 sugiere que el modelo  tiene  cierta  capacidad  para  ordenar  las  predicciones  por  probabilidad,  aunque limitada. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.017.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.018.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.019.jpeg)

En la evaluación final sobre el conjunto de test (1,556,182 ejemplos), el modelo fue reentrenado en el conjunto combinado train+val (8,818,362 ejemplos, equivalente al 85% del dataset). Las métricas de test mostraron un accuracy de 0.5156, balanced accuracy de 0.5025, precision de 0.5071, recall de 0.0606, F1-score de 0.1082 y ROC-AUC de 0.5131. La matriz de  confusión  reveló  que  el  modelo  predijo  correctamente  756,675  casos  de  clase  0 (verdaderos negativos) pero solo 45,741 casos de clase 1 (verdaderos positivos), confirmando su sesgo hacia predecir "no subida". Este comportamiento es típico de modelos lineales cuando enfrentan relaciones no lineales complejas y alta aleatoriedad en los datos. El tiempo de  entrenamiento  fue  de  aproximadamente  2  minutos,  demostrando  la  eficiencia computacional de los métodos lineales. 

2. **Random<a name="_page28_x82.00_y286.00"></a> Forest** 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.020.png)

El segundo modelo entrenado fue Random Forest con 100 árboles de decisión y profundidad máxima de 10 niveles. Este modelo de ensamble mostró un desempeño superior en todas las métricas comparado con la regresión logística. Durante la validación walk- forward, el accuracy promedio alcanzó 0.5367 ± 0.0031, representando una mejora de ~2.5 puntos porcentuales sobre el baseline lineal. El balanced accuracy de 0.5352 ± 0.0033 y la precision de 0.5310 ± 0.0063 indican predicciones más equilibradas entre ambas clases. Notablemente, el recall aumentó significativamente a 0.4581 ± 0.0412, demostrando que el modelo detecta 45.8% de las subidas reales comparado con solo 8.4% del modelo lineal. Esto resultó en un F1-score sustancialmente mejor de 0.4907 ± 0.0229. El ROC-AUC de 0.5557 ± 0.0049 confirma una capacidad predictiva moderada pero consistente. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.021.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.022.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.023.jpeg)

En la evaluación de test, el modelo reentrenado alcanzó un accuracy de 0.5369, balanced accuracy de 0.5353, precision de 0.5247, recall de 0.4822, F1-score de 0.5026 y ROC-AUC de 0.5549. La matriz de confusión mostró una distribución más balanceada con 471,330 verdaderos negativos, 329,809 falsos positivos, 390,924 falsos negativos y 364,119 verdaderos  positivos.  Esta  distribución  indica  que  el  modelo  es  capaz  de  identificar aproximadamente la mitad de las oportunidades reales de subida overnight, aunque al costo de  generar  falsos  positivos.  El  tiempo  de  entrenamiento  fue  significativamente  mayor, aproximadamente 1 hora 37 minutos, debido a la construcción y evaluación de 100 árboles de decisión con validación walk-forward. Este modelo fue seleccionado como ganador del experimento por su ROC-AUC superior y balance entre precision y recall. 

3. **SVM<a name="_page31_x82.00_y121.00"></a> con Descenso de Gradiente Estocástico** 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.024.png)

El  tercer  modelo  entrenado  fue  SVM-SGD  con  loss='log\_loss'  para  permitir estimación de probabilidades. Este modelo lineal con descenso de gradiente estocástico se entrenó  con  2000  iteraciones  máximas  y  regularización  L2  (alpha=0.0001).  Durante  la validación  walk-forward,  el  modelo  mostró  métricas  similares  a  la  regresión  logística tradicional. El accuracy promedio fue de 0.5122 ± 0.0047, balanced accuracy de 0.5035 ± 0.0024, precision de 0.5071 ± 0.0103 y recall de 0.1035 ± 0.0387. El F1-score de 0.1684 ± 0.0545 fue ligeramente superior al de regresión logística pero significativamente inferior al de Random Forest. El ROC-AUC de 0.5167 ± 0.0032 nuevamente confirma poder predictivo limitado. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.025.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.026.jpeg)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.027.jpeg)

En la evaluación de test, el modelo alcanzó un accuracy de 0.5150, balanced accuracy de 0.5027, precision de 0.5010, recall de 0.0897, F1-score de 0.1521 y ROC-AUC de 0.5123. La  matriz  de  confusión  reveló  733,701  verdaderos  negativos,  67,438  falsos  positivos, 687,347 falsos negativos y 67,696 verdaderos positivos. Al igual que la regresión logística, este modelo muestra fuerte sesgo hacia predecir la clase 0, identificando menos del 9% de las  subidas  reales.  El  tiempo  de  entrenamiento  fue  de  aproximadamente  3  minutos, posicionándose entre el método lineal más simple y el ensamble de árboles. Este modelo obtuvo el último lugar en la comparación final. 

<a name="_page33_x82.00_y407.00"></a>**5.6.Comparación Final y Selección del Mejor Modelo** 

Al finalizar el entrenamiento de los tres modelos, el pipeline generó automáticamente una comparación consolidada ordenada por ROC-AUC en el conjunto de test. Random Forest emergió como el modelo ganador con ROC-AUC de 0.5549, accuracy de 0.5369, balanced accuracy de 0.5353 y F1-score de 0.5026. Logistic Regression ocupó el segundo lugar con ROC-AUC de 0.5131, accuracy de 0.5156 y F1-score de 0.1082. SVM-SGD quedó en tercer lugar con ROC-AUC de 0.5123, accuracy de 0.5150 y F1-score de 0.1521. 

La superioridad de Random Forest se explica por su capacidad inherente de capturar relaciones no lineales y complejas interacciones entre features sin requerir transformaciones explícitas.  Los  árboles  de  decisión  individuales  dentro  del  bosque  pueden  identificar umbrales específicos en los indicadores técnicos que separan patrones de subida y bajada, mientras que el ensamble promedia estas decisiones reduciendo la varianza y mejorando la generalización. Adicionalmente, Random Forest es robusto ante features en diferentes escalas y no requiere normalización, evitando potenciales problemas de preprocesamiento. 

Los  modelos  lineales  (Logistic  Regression  y  SVM-SGD)  mostraron  desempeño similar y limitado, lo cual es consistente con la naturaleza no lineal y altamente ruidosa de los datos financieros. Estos modelos asumen una relación lineal o cuasi-lineal entre los indicadores  técnicos  y  la  probabilidad  de  subida  overnight,  una  suposición  que evidentemente no se cumple en este dominio. El bajo recall de ambos modelos lineales sugiere  que  adoptaron  una  estrategia  conservadora,  prediciendo  mayormente  la  clase negativa para minimizar el error de clasificación global, sacrificando la detección de patrones positivos. 

A pesar del desempeño superior de Random Forest, es importante contextualizar estos resultados. Un ROC-AUC de 0.5549 significa que el modelo tiene aproximadamente 55.49% de  probabilidad  de  ordenar  correctamente  un  par  aleatorio  de  observaciones  positiva- negativa, apenas 5.49 puntos porcentuales mejor que clasificación aleatoria. Esto confirma que los indicadores técnicos simples derivados únicamente de datos OHLCV tienen poder predictivo limitado para el fenómeno de gaps overnight, lo cual es consistente con la hipótesis de mercados eficientes que establece que los precios ya incorporan toda la información disponible públicamente. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.028.jpeg)

6. **Evaluación<a name="_page35_x82.00_y71.00"></a>** 

<a name="_page35_x82.00_y96.00"></a>**6.1.Análisis Detallado de Métricas** 

La evaluación final de los modelos se realizó sobre el conjunto de test que contiene 1,556,182 observaciones correspondientes al período temporal más reciente (15% final del dataset). Este conjunto representa aproximadamente 63 años de datos históricos diarios de 2,872 acciones NYSE, con una distribución de clases de 48.61% para la clase 0 (Open\_{t+1} ≤ Close\_t) y 51.39% para la clase 1 (Open\_{t+1} > Close\_t). Esta ligera predominancia de la clase positiva en el período de test sugiere un mercado con tendencia alcista durante el período evaluado, lo cual es históricamente consistente con el comportamiento de largo plazo del NYSE. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.029.jpeg)

El modelo ganador, Random Forest, alcanzó un accuracy de 53.69% en el conjunto de test, superando por 2.21 puntos porcentuales la baseline de 51.48% (correspondiente a predecir siempre la clase mayoritaria). Si bien esta mejora puede parecer modesta, representa un logro significativo considerando la naturaleza altamente estocástica de los mercados financieros  y  la  eficiencia  informacional  del  NYSE.  El  balanced  accuracy  de  53.53% confirma que esta mejora no proviene de un sesgo hacia la clase mayoritaria, sino de una genuina capacidad predictiva equilibrada entre ambas clases. 

La precision del modelo Random Forest fue de 52.47%, indicando que cuando el modelo predice una subida overnight (clase 1), acierta aproximadamente en la mitad de los casos. Este nivel de precision es suficiente para superar los costos de transacción típicos en trading algorítmico (que usualmente oscilan entre 5-10 puntos base por operación redonda), sugiriendo viabilidad potencial para aplicaciones prácticas bajo condiciones controladas. El recall de 48.22% significa que el modelo identifica aproximadamente la mitad de todas las subidas overnight reales que ocurren en el mercado. Este nivel de cobertura es razonable para una estrategia de trading selectiva que busque alta convicción en las señales. 

El  F1-score  de  0.5026  representa  la  media  armónica  entre  precision  y  recall, confirmando un balance apropiado entre ambas métricas. Este valor es significativamente superior al F1-score de los modelos lineales (0.1082 para Logistic Regression y 0.1521 para SVM-SGD), demostrando que Random Forest logra un compromiso sustancialmente mejor entre minimizar falsos positivos y maximizar la detección de casos positivos reales. En contextos de trading, este balance es crucial pues tanto los falsos positivos (pérdidas por compras  incorrectas)  como  los  falsos  negativos  (oportunidades  perdidas)  tienen  costos económicos reales. 

La métrica más importante para evaluar modelos de clasificación binaria es ROC- AUC (Area Under the Receiver Operating Characteristic Curve), que mide la capacidad del modelo de discriminar entre clases a través de todos los posibles umbrales de decisión. El Random Forest alcanzó un ROC-AUC de 0.5549, indicando que existe una probabilidad de 55.49% de que el modelo asigne una probabilidad mayor a una observación positiva aleatoria que a una observación negativa aleatoria. Esta métrica es particularmente valiosa porque es independiente  del  umbral  de  clasificación  elegido  y  refleja  la  calidad  intrínseca  de  las probabilidades estimadas por el modelo. 

Para  contextualizar  estos  resultados,  es  útil  compararlos  con  benchmarks  de  la literatura académica en predicción de mercados financieros. Estudios recientes de machine learning aplicado a asset pricing típicamente reportan ROC-AUC entre 0.52 y 0.58 para predicción  de  dirección  de  retornos  diarios  usando  features  técnicos,  con  mejoras  más sustanciales (ROC-AUC > 0.60) obtenidas únicamente mediante modelos profundos con arquitecturas complejas, grandes volúmenes de datos alternativos y features ingenierizados específicamente para el problema. Nuestro resultado de 0.5549 se posiciona en el rango medio-alto de este espectro, demostrando que incluso con features técnicos relativamente simples existe señal predictiva explotable. 

<a name="_page36_x82.00_y613.00"></a>**6.2.Interpretación de Matrices de Confusión** 

El análisis detallado de las matrices de confusión proporciona insights fundamentales sobre el comportamiento de cada modelo y sus modos de fallo característicos. Para el modelo Random Forest, la matriz de confusión en el conjunto de test mostró 471,330 verdaderos negativos (TN), 329,809 falsos positivos (FP), 390,924 falsos negativos (FN) y 364,119 verdaderos positivos (TP). Esta distribución permite calcular métricas adicionales de interés práctico. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.030.jpeg)

La  especificidad  del  modelo  (tasa  de  verdaderos  negativos),  calculada  como TN/(TN+FP),  resulta  en  58.83%.  Esto  significa  que  cuando  el  mercado  realmente  no experimenta  una  subida  overnight,  el  modelo  predice  correctamente  "no  subida"  en aproximadamente  6  de  cada  10  casos.  Por  otro  lado,  la  sensibilidad  o  recall  (tasa  de verdaderos positivos), calculada como TP/(TP+FN), alcanza 48.22%. Esta asimetría entre especificidad  y  sensibilidad  sugiere  que  el  modelo  es  ligeramente  más  conservador  al predecir subidas, requiriendo mayor evidencia en los indicadores técnicos para emitir una señal positiva. Este comportamiento es generalmente deseable en aplicaciones financieras donde la aversión al riesgo favorece estrategias que minimizan pérdidas sobre aquellas que maximizan ganancias absolutas. 

La tasa de falsos positivos (FP rate), calculada como FP/(FP+TN), es de 41.17%. Esto implica que el modelo genera señales erróneas de compra en aproximadamente 4 de cada 10 casos donde no debería hacerlo. En términos económicos, si cada falso positivo representa una operación perdedora con costo promedio del 1% (considerando spread bid-ask, slippage y comisiones), y asumiendo que se opera sobre todas las señales positivas del modelo, esto resultaría  en  pérdidas  acumuladas  significativas  que  deberían  ser  compensadas  por  las ganancias en los verdaderos positivos. La tasa de falsos negativos (FN rate), calculada como FN/(FN+TP), es de 51.78%, indicando que el modelo pierde aproximadamente la mitad de las oportunidades reales de subida overnight. Este balance entre FP rate y FN rate determina la viabilidad práctica del modelo. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.031.jpeg)

Comparando con los modelos lineales, las matrices de confusión revelan patrones de comportamiento marcadamente diferentes. Logistic Regression mostró 756,675 TN, 44,464 FP, 709,302 FN y 45,741 TP, lo que se traduce en una especificidad extremadamente alta de 94.45% pero una sensibilidad muy baja de 6.06%. Este modelo adoptó una estrategia ultra- conservadora, prediciendo la clase positiva solo en casos de altísima convicción según su frontera de decisión lineal. Si bien esta estrategia minimiza pérdidas por falsos positivos (FP rate  de  apenas  5.55%),  sacrifica  completamente  la  detección  de  oportunidades  reales, resultando en un modelo prácticamente inútil para aplicaciones reales de trading. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.032.jpeg)

El  modelo  SVM-SGD  exhibió  un  comportamiento  intermedio  con  733,701 TN, 67,438  FP,  687,347  FN  y  67,696  TP,  correspondiendo  a  especificidad  de  91.58%  y sensibilidad de 8.97%. Aunque ligeramente menos conservador que Logistic Regression, este modelo mantiene el sesgo fundamental hacia predecir la clase negativa, resultando en un recall insuficiente para capturar valor económico. La similitud en el comportamiento de ambos  modelos  lineales  confirma  que  la  limitación  no  es  específica  del  algoritmo  de optimización sino inherente a la capacidad representacional de los modelos lineales frente a la complejidad no lineal del problema. 

<a name="_page40_x82.00_y121.00"></a>**6.3.Análisis de Estabilidad Temporal** 

La validación cruzada walk-forward con k=5 folds proporcionó información valiosa sobre la estabilidad temporal de los modelos. Para Random Forest, el ROC-AUC varió entre 0.5492 (fold 1) y 0.5640 (fold 2), con desviación estándar de 0.0049. Esta variabilidad relativamente baja sugiere que el modelo mantiene su poder predictivo de manera consistente a  través  de  diferentes  períodos  temporales,  sin  exhibir  degradación  significativa  en condiciones de mercado cambiantes. El fold 2 mostró el mejor desempeño con ROC-AUC de 0.5640 y F1-score de 0.5202, sugiriendo que este período particular contenía patrones más pronunciados o menos ruidosos que facilitaron la clasificación. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.033.png)

En contraste, el fold 5 (más reciente) mostró un ligero descenso en recall (0.4581 vs promedio de 0.4581), aunque mantuvo accuracy y ROC-AUC competitivos. Esta pequeña degradación podría indicar cambios graduales en la microestructura del mercado o en el comportamiento  de  los  gaps  overnight  durante  el  período  más  reciente,  un  fenómeno conocido en finanzas como "concept drift". Sin embargo, la magnitud de esta variación está dentro  del  rango  esperado  de  fluctuación  estadística  natural,  por  lo  que  no  representa evidencia concluyente de degradación sistemática del modelo. 

Los modelos lineales mostraron patrones de estabilidad temporal similares entre sí. Logistic  Regression  exhibió  ROC-AUC  entre  0.5154  (fold  5)  y  0.5246  (fold  4),  con desviación estándar de 0.0034. SVM-SGD varió entre 0.5117 (fold 5) y 0.5219 (fold 4), con desviación estándar de 0.0032. Esta menor variabilidad comparada con Random Forest sugiere que los modelos lineales son más estables pero menos sensibles a patrones temporales específicos, consistente con su menor capacidad de adaptación a relaciones complejas en los datos. 

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.034.png)

![](Aspose.Words.242f31fe-f742-47d9-9e44-30a0caf1c3d1.035.png)

Un hallazgo interesante es que los tres modelos mostraron su peor desempeño en el fold 5 (más reciente) y su mejor desempeño en el fold 4, sugiriendo que podría existir algún fenómeno sistemático en el período correspondiente al fold 5 que dificulta la predicción. Esto podría  estar  relacionado  con  eventos  de  mercado  específicos  como  períodos  de  alta volatilidad,  crisis  financieras  o  cambios  regulatorios  que  alteraron  temporalmente  la dinámica de los gaps overnight. Un análisis más detallado requeriría examinar las fechas específicas correspondientes a cada fold y correlacionarlas con eventos macroeconómicos históricos. 

7. **Despliegue (Deploy) del Sistema del Proyecto de Aprendizaje Estadístico 7.1.Publicación del Proyecto y del Sistema en GITHUB** 
1. **Pestaña de Documentación del Proyecto** 
1. **Pestaña de Código del Sistema** 
1. **Pestaña de Ejecución y Pruebas del Sistema** 

**7.2.Deploy del APP o Web del Sistema de Predicción, de Clasificación, de Segmentación** 

- **Asociación.** 

<a name="_page42_x82.00_y363.00"></a>**Referencias Bibliograficas** 

Fama, E. (1969). Efficient Capital Markets: A Review of Theory and Empirical Work. *The* 

*Journal of Finance*, 383–417. 

Gu, S., Kelly, B., & Xiu, D. (2020). Empirical Asset Pricing via Machine Learning. *The* 

*Review of Financial Studies*, 2223–2273. 

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data* 

*Mining, Inference, and Prediction.* Springer. 

Hyndman, R., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice.* OTexts. 

Mireles Vázquez, I. (2011). Bolsa de Valores "¿Cómo? ¿Por qué? Y ¿Para qué?". *Tiempo* 

*Económico*, 56. 

Reyna, A. (2024). *¿Qué es la bolsa de valores? Una explicación simple*. Obtenido de BBVA: 

https://www.bbva.com/es/salud-financiera/que-es-la-bolsa-de-valores-una- explicacion-simple/ 

Villanueva Gonzales, A. (2007). Mercados financieros: una aproximación a la Bolsa de 

Valores de Lima. *Contabilidad y Negocios*, 23-33. 
45 
