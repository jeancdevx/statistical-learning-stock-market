**Universidad Privada Antenor Orrego** 

**Facultad de Ingeniería** 

**Programa de Estudio de Ingeniería de Sistemas e Inteligencia Artificial** 

![](Aspose.Words.ccc5bea3-c0b5-4595-9c89-688e86b3c3b6.001.png)

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

5\.1.  Entrenamiento  del  Modelo:  Aplicación  al  Modelo:  uso  del  Data-Set  de Entrenamiento y de Prueba ............................................... **¡Error! Marcador no definido.** 

6. [Evaluación .................................................................................................................... 16 ](#_page15_x82.00_y234.00)[Bibliografía ........................................................................................................................... 17 ](#_page16_x82.00_y71.00)
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

**5.1.Construcción de la matriz de aprendizaje** 

6. **Evaluación<a name="_page15_x82.00_y234.00"></a>** 

<a name="_page16_x82.00_y71.00"></a>**Bibliografía** 

Fama, E. (1969). Efficient Capital Markets: A Review of Theory and Empirical Work. *The* 

*Journal of Finance*, 383–417. 

Gu, S., Kelly, B., & Xiu, D. (2020). Empirical Asset Pricing via Machine Learning. *The* 

*Review of Financial Studies*, 2223–2273. 

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data* 

*Mining, Inference, and Prediction.* Springer. 

Hyndman, R., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice.* OTexts. 

Mireles Vázquez, I. (2011). Bolsa de Valores "¿Cómo? ¿Por qué? Y ¿Para qué?". *Tiempo* 

*Económico*, 56. 

Reyna, A. (2024). *¿Qué es la bolsa de valores? Una explicación simple*. Retrieved from 

BBVA:  https://www.bbva.com/es/salud-financiera/que-es-la-bolsa-de-valores-una- explicacion-simple/ 

Villanueva Gonzales, A. (2007). Mercados financieros: una aproximación a la Bolsa de 

Valores de Lima. *Contabilidad y Negocios*, 23-33. 
17 
