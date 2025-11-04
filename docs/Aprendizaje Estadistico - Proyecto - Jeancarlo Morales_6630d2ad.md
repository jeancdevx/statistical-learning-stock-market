Universidad Privada Antenor Orrego

Facultad de Ingeniería

Programa de Estudio de Ingeniería de Sistemas e Inteligencia Artificial

Curso: Aprendizaje Estadístico

Proyecto Semestral

“Modelado y análisis predictivo de precios de acciones en el mercado bursátil

mediante técnicas avanzadas de aprendizaje estadístico”

Equipo de Trabajo

Olazabal Ávila Fernando

Kong Carranza Luis

Morales Robles Jeancarlo (coordinador)

León García Axel

Gastañuadi Iturri, Efrain

Tarazona Flores José

Albitres Dávila Juan

Docente: Hernan Sagastegui Chigne

Trujillo – 21 de septiembre del 2025

Aprendizaje Estadístico

Proyecto Semestral

Índice del Contenido

Índice del Contenido ............................................................................................................... 2

1.

Introducción .................................................................................................................... 4

1.1.

Título del Proyecto ................................................................................................. 4

1.2.  Antecedentes ........................................................................................................... 4

1.3.

Problema a resolver ................................................................................................ 6

1.4.  Objetivos ................................................................................................................. 6

1.4.1.

Objetivo general: ............................................................................................ 6

1.4.2.

Objetivos específicos: ..................................................................................... 6

2.  Requerimientos ............................................................................................................... 7

2.1.  Definición del dominio ........................................................................................... 7

2.2.  Determinación de requisitos (requerimientos) ....................................................... 8

3.  Pre-Procesamiento y Normalización .............................................................................. 9

3.1.  Medidas, Datos, Bases de Datos y Elaboración del Data-Set ................................ 9

3.2.  Normalización y/o Filtrado de Datos ..................................................................... 9

3.3.

Planteamiento de la Organización del Data-Set ................................................... 10

3.3.1.

Data-Set de entrenamiento (training) ........................................................... 10

3.3.2.

Data-Set de Pruebas (test)............................................................................. 10

3.3.3.

Data-Set de Validación ("Cross-Validation") ................................................ 10

4.  Aprendizaje ................................................................................................................... 11

4.1.

Planteamiento del modelo de aprendizaje ............................................................ 11

4.2.  Desarrollo e implementación del modelo ............................................................. 12

5.  Comprobación .............................................................................................................. 15

5.1.  Aplicación al Modelo: uso del Data-Set de Entrenamiento y de Prueba..... ¡Error!

Marcador no definido.

2

Aprendizaje Estadístico

Proyecto Semestral

6.  Evaluación .................................................................................................................... 20

Bibliografía ........................................................................................................................... 23

3

Aprendizaje Estadístico

Proyecto Semestral

1.  Introducción

1.1.Título del Proyecto

Modelado y análisis predictivo de la dirección del precio de apertura en acciones del

NYSE mediante técnicas de aprendizaje estadístico.

1.2.Antecedentes

La bolsa de valores es una organización privada que brinda las facilidades necesarias

para que sus miembros (corredores o intermediarios), atendiendo los mandatos de sus clientes

(demandantes y oferentes), introduzcan órdenes y realicen negociaciones de compra y venta

de  valores,  tales  como  acciones  de  sociedades  o  compañas  anónimas,  bonos  públicos  y

privados,  certificados,  títulos  de  participación  y  una  amplia  variedad  de  instrumentos  de

inversión  (Mireles  Vázquez,  2011).  La  característica  de  la  bolsa  de  valores  es  que  se

comercializan instrumentos financieros, las personas que compran esos instrumentos se les

conoce como inversionistas y las personas o entidades que colocan o “venden”, se les conoce

como emisores (Reyna, 2024).

Desde una perspectiva económica, la bolsa de valores constituye una institución del

mercado  encargada  de  articular  la  interacción  entre  la  oferta  y  la  demanda  de  activos

financieros,  posibilitando  la  determinación  eficiente  de  sus  precios.  Se  entiende  que  un

mercado alcanza eficiencia cuando los agentes que en él participan disponen de la totalidad

de la información pertinente y los precios de los activos negociados incorporan de manera

adecuada dicha información (Villanueva Gonzales, 2007).

El término “bolsa” tiene su origen en la ciudad de Brujas, ubicada en la región de

Flandes, donde existía un edificio perteneciente a la familia noble Van Der Buërse. En dicho

lugar se llevaban a cabo reuniones y transacciones de carácter mercantil. El blasón de esta

familia  mostraba  tres  bolsas  de  piel,  que  en  aquel  periodo  representaban  los  monederos

utilizados. Debido a la relevancia de las operaciones comerciales realizadas, así como a la

influencia social y económica de la familia, el  apellido  Buërse dio  nombre a lo  que en la

actualidad se conoce como bolsa (Mireles Vázquez, 2011).

4

Aprendizaje Estadístico

Proyecto Semestral

La  mayoría  de  los  países  disponen  de  una  bolsa  de  valores;  sin  embargo,  la  más

relevante a nivel mundial es la Bolsa de Nueva York (NYSE), reconocida por su volumen de

transacciones  y  por  el  número  de  compañías  que  en  ella  cotizan.  En  segundo  lugar,  se

encuentra  el  NASDAQ,  considerado  el  mayor  mercado  automatizado  de  valores  en  los

Estados  Unidos,  cuya  particularidad  radica  en  la  concentración  de  empresas  vinculadas

principalmente a los sectores de alta tecnología, tales como la electrónica, la informática y

las telecomunicaciones, entre otros (Reyna, 2024).

Fama expone las formas de eficiencia de mercado (débil, semi-fuerte, fuerte) y discute

qué  implicaciones  tiene  la  disponibilidad  de  información  sobre  la  capacidad  de  predecir

retornos. Es esencial para justificar por qué algunos enfoques predictivos podrían fallar o por

qué habría que buscar señales no lineales/alternativas (Fama, 1969).

Con  la  entrada  del  machine  learning  en  finanzas,  trabajos  recientes  muestran  que

métodos  no  lineales  (árboles,  boosting,  redes  neuronales,  ensembles)  pueden  mejorar  la

predicción  de  primas  de  riesgo  y  retornos  esperados  frente  a  regresiones  lineales

tradicionales,  en  particular  cuando  los  modelos  explotan  interacciones  complejas  entre

cientos de predictores y usan procedimientos de regularización y validación adecuados (Gu,

Kelly, & Xiu, 2020).

En paralelo, el aprendizaje estadístico amplió el repertorio con métodos predictivos y

de clasificación/ regresión regularizada, árboles y ensambles y máquinas de soporte vectorial,

prestando especial atención a la validación y al control del sobreajuste (Hastie, Tibshirani, &

Friedman,  2009).  En  mercados  accionarios  líquidos  como  la  New York  Stock  Exchange

(NYSE), estos enfoques se aplican sobre representaciones transformadas de los precios (p.

ej.,

rendimientos

logarítmicos)

y

sobre

características

derivadas

(rezagos,

medias/volatilidades móviles, cruces de medias, momentum), buscando identificar señales

predictivas  débiles  pero  explotables  dentro  de  un  esquema  de  validación  temporal  (walk-

forward)  y  métricas  adecuadas  tanto  para  clasificación  (dirección:  sube/baja)  como  para

regresión (Hyndman & Athanasopoulos, 2021).

5

Aprendizaje Estadístico

Proyecto Semestral

1.3.Problema a resolver

El  proyecto  aborda  la  siguiente  pregunta  aplicada:  ¿es  posible  identificar  señales

predictivas  estadísticamente  significativas  en  la  dirección  del  precio  de  apertura  del  día

siguiente  (sube  o  baja  respecto  al  cierre  previo)  para  acciones  del  NYSE  utilizando

exclusivamente  técnicas  de  aprendizaje  estadístico  basadas  en  series  históricas  OHLCV  e

indicadores  técnicos  derivados?  En  términos  operativos,  se  formulará  un  problema  de

clasificación  binaria  con  etiqueta  𝑦𝑡+1 = 𝟏[Open𝑡+1 > Close𝑡],  empleando  variables
construidas  a  partir  de  retornos,  volatilidad,  promedios  móviles,  momentum  y  relaciones

precio–volumen. Bajo la hipótesis de eficiencia semi-fuerte del mercado (Fama, 1969), se

espera que información pública histórica tenga poder predictivo limitado pero explotable. El

objetivo no es alcanzar precisiones del 80-90% (lo cual sugeriría ineficiencias severas), sino

demostrar que modelos supervisados pueden superar significativamente el baseline aleatorio

(50%) y cuantificar el límite superior de predicción con features exclusivamente técnicos. Se

considera éxito del modelo: (1) ROC-AUC significativamente superior a 0.50 (p < 0.05), (2)

Balanced Accuracy > 52% en test, (3) estabilidad en validación walk-forward (desviación

estándar  <  2%),  y  (4)  superioridad  estadística  frente  a  baseline  naive  (predecir  clase

mayoritaria).

1.4.Objetivos

1.4.1.  Objetivo general:

Desarrollar  y  evaluar  un  modelo  de  aprendizaje  supervisado  capaz  de  predecir  la

dirección  del  precio  de  apertura  del  día  siguiente  en  acciones  del  NYSE,  utilizando

únicamente  información  histórica  de  mercado  y  técnicas  de  aprendizaje  estadístico,  con

evaluación rigurosa mediante validación cruzada y métricas apropiadas de clasificación.

1.4.2.  Objetivos específicos:

Definir el conjunto de variables predictoras a partir de precios y volumen (retornos,

indicadores técnicos y rezagos), documentando su relación con la variable objetivo.

Construir los conjuntos de entrenamiento, validación y prueba respetando el orden

temporal.

6

Aprendizaje Estadístico

Proyecto Semestral

Entrenar y comparar modelos de clasificación alineados al sílabo del curso regresión

logística,  árboles  de  decisión,  SVM,  KNN,  discriminante  lineal/naïve  Bayes  bajo  un

protocolo común de validación y selección de características.

Seleccionar el modelo con mejor desempeño fuera de muestra según métricas como

exactitud, F1 y balanced accuracy, reportando intervalos/variabilidad por validación cruzada.

Analizar la estabilidad del modelo ante cambios de ventanas temporales y universos

de acciones, discutiendo sus limitaciones y alcances.

2.  Requerimientos

2.1.Definición del dominio

El dominio del proyecto es la predicción de la dirección del precio de apertura del día

siguiente (sube o baja respecto al día previo) en acciones que cotizan en la Bolsa de Nueva

York  (NYSE).  Se  modelará  como  un  problema  de  clasificación  binaria  supervisada,

coherente  con  los  contenidos  del  curso  (regresión  y  clasificación;  árboles  de  decisión;

máquinas de soporte vectorial; y evaluación del rendimiento), lo que permite aplicar técnicas

vistas formalmente en la asignatura y medir su capacidad de generalizar en datos no vistos.

En  este  contexto,  La  variable  objetivo  será  un  indicador  binario  construido  a  partir  de  la

comparación entre la apertura en 𝑡 + 1y el cierre en 𝑡: 𝑦𝑡+1 = 𝟏[Open𝑡+1 > Close𝑡]. Las
variables explicativas provendrán de series históricas diarias de precios y volumen (OHLCV)

y de indicadores técnicos derivados, retornos y log-retornos, promedios móviles simples y

exponenciales,  osciladores  de  momentum,  medidas  de  volatilidad  y  relaciones  precio–

volumen junto con rezagos que capturen dependencia temporal. El fenómeno a modelar es

no estacionario y con alta relación señal–ruido: la dinámica de precios cambia por eventos

macro, microestructura del mercado y comportamiento de inversionistas, por lo que el diseño

debe contemplar división temporal estricta de los datos, evitar “fugas de información” (look-

ahead  bias)  y  usar  validación  apropiada  para  series  temporales.  Además,  el  objetivo

pedagógico es demostrar, en un caso real de finanzas, cómo se ajusta, evalúa y optimiza un

clasificador  en  línea  con  los  resultados  de  aprendizaje  del  curso,  que  enfatizan  técnicas

supervisadas y su evaluación con validación cruzada y métricas de rendimiento.

7

Aprendizaje Estadístico

Proyecto Semestral

2.2.Determinación de requisitos (requerimientos)

Para garantizar un estudio riguroso y realista, los requisitos se organizan en datos,

metodología, evaluación, herramientas y consideraciones operativas.

En  datos,  se  requiere  una  fuente  pública  y  consistente  de  series  diarias  (apertura,

máximo,  mínimo,  cierre,  volumen)  con  historial  suficiente  para  construir  ventanas  de

entrenamiento, validación y prueba. Se trabajará con un subconjunto manejable de acciones

líquidas del NYSE, manteniendo el orden temporal en todos los pasos. El dataset incluirá la

etiqueta  binaria  de  dirección  de  apertura  𝑦𝑡+1 = 𝟏[Open𝑡+1 > Close𝑡]y  un  conjunto  de
predictores derivados de series OHLCV, calculados solo con información disponible hasta 𝑡..

En metodología de aprendizaje, el sistema debe implementar un pipeline supervisado:

(1)

preparación

del

dataset

con

separaciones

temporales

claras;

(2)

estandarización/normalización cuando el algoritmo lo requiera; (3) entrenamiento de varios

clasificadores coherentes con el sílabo, por ejemplo, regresión logística, árboles de decisión,

SVM, KNN, naïve Bayes y análisis discriminante; (4) selección y ajuste de hiperparámetros

con  validación  cruzada  compatible  con  series  temporales;  y  (5)  comparación  justa  entre

modelos bajo el mismo protocolo de partición y métricas. Estas familias de modelos y su

evaluación forman parte explícita de los contenidos de la asignatura.

En  evaluación,  el  requisito  es  estimar  desempeño  fuera  de  muestra  con  métricas

acordes a clasificación binaria. Se tomará como mínimo Accuracy para comparar con una

línea base ingenua (por ejemplo, “siempre igual a la clase mayoritaria”), complementando

con  F1-score  cuando  exista  desbalance  y  ROC-AUC  para  sensibilidad  a  umbrales.  La

evaluación usará validación cruzada (k-fold temporal o bloques) para seleccionar el modelo

y un conjunto de prueba estrictamente posterior en el tiempo para reporte final, como enfatiza

el  curso  al  incorporar  validación  cruzada  y  métricas  de  rendimiento  en  sus  resultados  de

aprendizaje y contenidos.

En herramientas y reproducibilidad, se requiere un entorno práctico de análisis con

Python  y  bibliotecas  estándar  para  ciencia  de  datos,  control  de  versiones  de

notebooks/código,  bitácora  de  experimentos  y  documentación  clara  del  pipeline  (desde  la

descarga de datos hasta el reporte de resultados).

8

Aprendizaje Estadístico

Proyecto Semestral

En consideraciones operativas y alcance, el sistema es estrictamente académico: no

ejecutará órdenes de mercado ni incluirá costos de transacción; su objetivo es evaluar si un

clasificador  puede  acertar  la  dirección  con  significancia  frente  a  una  línea  base,  discutir

limitaciones  (no  estacionariedad,  posible  sobreajuste,  deriva  de  concepto)  y  proponer

estrategias de mejora (nuevas variables, ventanas rodantes y reentrenamiento periódico).

3.  Pre-Procesamiento y Normalización

3.1.Medidas, Datos, Bases de Datos y Elaboración del Data-Set

El proyecto utiliza un único dataset masivo y vigente: el paquete U.S. – daily (ASCII)

de  Stooq,  del  cual  se  filtra  exclusivamente  el  universo  NYSE  (se  excluyen  ETFs  y  otros

mercados). La fecha de corte del estudio se fija en 16 de enero del 1961 al 31 de octubre de

2025; toda la extracción y el procesamiento se documentan con esa fecha.

A partir de los archivos diarios OHLCV (Open, High, Low, Close, Volume) por ticker,

se construye un panel (Ticker,Date)ordenado cronológicamente, con control de duplicados y

verificación

básica

de

calidad

(fechas

de  mercado

y

campos

críticos).

Variable objetivo (dirección overnight). Para cada ticker y día 𝑡:

𝑦𝑡+1 = 𝟏[Open𝑡+1 > Close𝑡].

Predictores  (solo  hasta  𝑡).  (a)  Retornos  log:  ret_cc_1,ret_oo_1,ret_co_1;  (b)

Tendencia/momentum:  SMA(5),SMA(10),EMA(10), mom5;  (c)  Volatilidad  y  rango:

std5, std10, range_rel = (High − Low)/Close; (d) Volumen: vol_ma_10,vol_rel = Volume/

MA10(Volume); (e) Calendario: dow(día de la semana). Todas las ventanas terminan en 𝑡; se

descartan filas de warm-up hasta completar ventanas (p. ej., 𝑤 = 10).

3.2.Normalización y/o Filtrado de Datos

La normalización es clave para modelos sensibles a escala (SVM, KNN, regresión

logística).  Se  utilizará  estandarización  z-score  por  ticker  —media  y  desviación  estándar

calculadas sólo en el conjunto de entrenamiento— y aplicadas luego a validación y prueba

para  impedir  fuga  de  información.  Como  robustez  ante  colas  pesadas,  se  considerará

winsorización por variable (recorte en percentiles 1 %–99 %) o escalado robusto (mediana e

IQR) cuando se detecten outliers extremos en volumen o rangos de precio. Para indicadores

9

Aprendizaje Estadístico

Proyecto Semestral

acumulativos como OBV, se preferirá normalizarlos por su desviación rodante o convertirlos

a cambios porcentuales para hacerlos comparables entre tickers.

El filtrado incluirá: eliminación de filas con datos faltantes críticos para el cálculo de

la etiqueta (si falta Open en  to t + 1); descarte de las primeras wobservaciones por ticker

(periodo de warm-up necesario para indicadores con ventanas de wdías); y control de calidad

de fechas de mercado (excluyendo cierres no bursátiles). Para reducir sesgo de supervivencia,

el  panel  se  construirá  tal  como  aparece  en  la  fuente  durante  el  periodo  estudiado;  si  se

complementa con una fuente dinámica (yfinance), se congelará una “foto” de tickers al inicio

del periodo de análisis y se documentará la lista utilizada. En todos los casos, se conservará

la  temporalidad:  cualquier  estadístico  de  escalado  o  selección  de  características  se  ajusta

antes de ver validación/prueba.

3.3.Planteamiento de la Organización del Data-Set

3.3.1.  Data-Set de entrenamiento (training)

75%  Entrenamiento  (training).  Comprende  desde  el  inicio  del  historial  hasta  el

percentil  temporal  75.  En  este  bloque  se  ajustan  los  modelos  base  y  se  calculan

exclusivamente  aquí  todos  los  parámetros  de  pre-procesamiento  (p.  ej.,  medias  y

desviaciones para estandarización, winsorización, selección de variables). Esto maximiza la

cantidad de ejemplos que ven los algoritmos y reduce la varianza de los estimadores.

3.3.2.  Data-Set de Pruebas (test)

15% Prueba (test). Es el tramo final (del 85% al 100%) y no interviene en decisiones

de modelado. Se usa una única vez para estimar desempeño fuera de muestra en condiciones

realistas, pues captura el período más reciente (y potencialmente más difícil) del mercado.

3.3.3.  Data-Set de Validación ("Cross-Validation")

10% Validación  para  “Cross-Validation”.  Corresponde  al  tramo  temporal  siguiente

(del 75% al 85%). Este bloque se utiliza para seleccionar hiperparámetros y afinar decisiones

como  umbrales  de  clasificación  o  regularización.  La  validación  se  implementa  con  un

esquema  walk-forward  sobre  ese  10%:  se  divide  en  𝑘 = 5subbloques  contiguos.  En  cada

fold, se reentrena con el 75% inicial más los subbloques ya vistos, y se valida en el subbloque

inmediatamente posterior, respetando el flujo temporal y evitando look-ahead. Al finalizar,

10

Aprendizaje Estadístico

Proyecto Semestral

se reentrena el modelo ganador sobre el 85% (75%+10%) Así se respeta el flujo temporal

(entreno-antes / valido-después), se evalúa robustez frente a pequeñas derivas del mercado y

se evita fuga de información. Concluida esta etapa, se reentrena el modelo ganador sobre el

85% acumulado (75% + 10%) con los hiperparámetros óptimos.

4.  Aprendizaje

4.1.Planteamiento del modelo de aprendizaje

El problema se formula como clasificación binaria supervisada: para cada acción y

día 𝑡, se busca predecir la dirección de la apertura del día 𝑡 + 1respecto al cierre del día 𝑡(gap

“overnight”). La etiqueta es 𝑦𝑡+1 = 1[Open𝑡+1 > Close𝑡]..

Desde una perspectiva de aprendizaje estadístico, el plan contempla dos familias de

modelos complementarios:

Modelo lineal interpretable (Regresión Logística con regularización 𝐿2): sirve como

línea  base  robusta  y  explicable.  Permite  cuantificar  el  efecto  marginal  de  señales  de

“momentum”, volatilidad y microestructura sobre la probabilidad de alza en la apertura.

Modelo no lineal de mayor capacidad (árboles potenciados tipo Gradient Boosting

/ Random Forest o, alternativamente, un SVM con kernel RBF si la dimensionalidad efectiva

es moderada): capturan interacciones y umbrales que los lineales no expresan. Estos modelos

se justifican porque la dinámica overnight suele ser no lineal y dependiente del régimen (p.

ej., volatilidad reciente, shocks de volumen o rangos intradía).

La variable de entrada 𝑋𝑡se compone exclusivamente de información conocida al

cierre del día 𝑡, para evitar fuga de información. Se agrupa en cuatro bloques realistas y

computables con datos diarios:

•  Precio/retornos  y  momentum:  retornos  log  de  1,  2,  5  y  10  días;  retorno  intradía

(Close𝑡/Open𝑡 − 1);  cruces  y  desviaciones  de  medias  móviles  (p.  ej.,  Close𝑡vs.
SMA(5), SMA(10)); osciladores simples como %K (suavizado con ventana corta).

•  Rango  y  volatilidad:  rango  normalizado  (High𝑡 − Low𝑡)/Close𝑡,  “true  range”  y
desviación estándar móvil de retornos (5 y 10 días) como proxy de volatilidad.

11

Aprendizaje Estadístico

Proyecto Semestral

•  Volumen y presión de orden: cambio porcentual de volumen vs. su media móvil (5

y 10 días); volumen relativo (vol/avgVol); On-Balance Volume incremental.

•  Factores  de mercado/sector y calendario  (opcionales si  están  disponibles en el

dataset): retorno del índice amplio (p. ej., S&P500/ETF proxy) y de su sector el día

𝑡; cambio del VIX si está disponible; dummies de día de la semana y fin de mes, para

capturar patrones estacionales simples.

La  hipótesis  de  trabajo  es  que  combinaciones  parsimoniosas  de  estas  señales—

normalizadas y con rezagos—aportan probabilidad predictiva superior al 50% en la dirección

overnight para acciones líquidas del NYSE. En términos de sesgo–varianza, el modelo lineal

da un piso estable (más sesgo, menos varianza) y el modelo de árboles/SVM intenta capturar

no linealidades (menos sesgo, más varianza), controlando complejidad con regularización y

validación  apropiada.  De  esta  forma,  el  proyecto  contrasta  interpretabilidad  vs.  poder

predictivo dentro de un mismo marco experimental.

4.2.Desarrollo e implementación del modelo

La implementación se realiza con un pipeline reproducible en Python (scikit-learn) o,

de requerirse evidencia en herramientas del curso, con WEKA para las versiones lineales y

de árboles. El flujo está diseñado para respetar la estructura temporal y el split 75%/10%/15%

ya definido:

1.  Construcción de la matriz de aprendizaje (por ticker y luego apilada):

o  Ordenamiento cronológico estricto.

o  Cálculo  de  todas  las  características  con  ventanas  que  terminan  en  𝑡;

cualquier estadístico que use 𝑡 + 1se descarta.

o  Etiquetado según la definición de gap 𝑦𝑡+1 = 𝟏[Open𝑡+1 > Close𝑡].

2.  Preprocesamiento dentro de un Pipeline:

o  Imputación  de  faltantes  sólo  con  estadísticas  del  entrenamiento  (median

imputer).

12

Aprendizaje Estadístico

Proyecto Semestral

o  Normalización/estandarización de variables continuas con medias y desvíos

del entrenamiento.

o  Winsorización suave de colas (percentiles 1–99) para robustez a outliers.

o  Opcional: estandarización cross-seccional por día (z-score por jornada) si

se entrenará un único modelo “apilado” para múltiples acciones; esto reduce

el drift de escala entre tickers.

3.  Partición temporal y validación:

o  Se  respeta  el  acuerdo  del  curso:  75%  entrenamiento,  15%  prueba,  10%

validación por cross-validation. Operativamente, se procede así:

▪  Con  el  75%  de  entrenamiento  se  realiza  una  validación  cruzada

temporal  (k-fold  no  aleatorio/“expanding  window”  o  “walk-

forward”) para ajustar hiperparámetros y seleccionar variables.

▪  El  15%  test  queda  completamente  bloqueado  hasta  el  final  para

estimar desempeño fuera de muestra.

▪  El  10%  restante  puede  emplearse  como  hold-out  adicional  o

integrarse  al  esquema  de  CV  como  último  bloque  “de  validación

externa” para verificar estabilidad.

o  Se fija semilla aleatoria y se loguean versiones para reproducibilidad.

4.  Modelos y ajuste de hiperparámetros (con búsqueda en malla/aleatoria dentro de

la CV temporal):

o  Regresión  Logística  𝐿2:  𝐶(inversa  de  la  regularización),  opción  de

class_weight='balanced' si hay leve desbalance.

o  Modelo no lineal (elegir uno para el informe principal y dejar el otro como

robustez):

▪  Gradient Boosting / XGBoost equivalente: n_estimators (100–500),

learning_rate  (0.01–0.1),  max_depth  (2–4),  subsample  (0.6–1.0),

min_samples_leaf.

13

Aprendizaje Estadístico

Proyecto Semestral

▪  SVM:  kernel  (lineal  o  RBF),  𝐶y  𝛾para  RBF;  escalar  siempre  las

entradas.

o  Selección  de  variables  opcional  guiada  por  importancia  (árboles)  o  por

penalización  (logística  con  𝐿1en  una  corrida  auxiliar)  para  reducir

colinealidad y ruido.

5.  Métricas primarias y control de sobreajuste dentro de la CV:

o  Accuracy direccional y Balanced Accuracy (por si hay asimetría en clases),

F1 y ROC-AUC como apoyo.

o  Estabilidad temporal: comparar desempeño por subperíodos dentro de la CV

(ej., años o trimestres) para detectar dependencia de régimen.

o  Curva  de  calibración  del  modelo  probabilístico

(sobre

todo  en

logística/boosting) y ajuste de umbral de decisión (por ejemplo, operar sólo

si 𝑃(𝑦 = 1) > 0.55).

6.  Reglas prácticas para despliegue experimental (sin trading algorítmico complejo,

sólo para validar realismo):

o  Generar  una  señal  “comprar  en  apertura”  si  el  modelo  predice  subida

overnight  con  probabilidad  por  encima  del  umbral;  “no  operar”  en  caso

contrario.

o  Evaluar  una  métrica  económica  ilustrativa  en  el  set  de  prueba  (se

desarrollará  formalmente  en  la  sección V):  tasa  de  aciertos  condicionada  a

señal, retorno medio por operación neto de un costo fijo conservador (p. ej.,

5–10 bps), y “hit ratio vs. benchmark 50%”.

o  Evitar  look-ahead  y  survivorship  bias:  los  cálculos  usan  sólo  datos

disponibles al cierre de 𝑡y se mantienen tickers constantes durante el período

evaluado.

7.  Buenas prácticas y entregables técnicos:

14

Aprendizaje Estadístico

Proyecto Semestral

o  Pipeline  de  scikit-learn  que  encadena  preprocesamiento  y  modelo  para

impedir fugas.

o  TimeSeriesSplit para la CV; gráficos de importancia de variables (árboles) y

coeficientes (logística) con sus signos, discutidos en lenguaje claro.

o  Cuaderno  Colab  y  README  con  instrucciones,  versiones  de  librerías,

semillas y tiempos de corrida.

o  Si  se  requiere,  ARFF  para  cargar  el  dataset  ya  preprocesado  en  WEKA  y

replicar la logística y un árbol de decisión con su evaluación.

5.  Comprobación

5.1.Entrenamiento  del  Modelo:  Aplicación  al  Modelo:  uso  del  Data-Set  de

Entrenamiento y de Prueba

5.1.1.  Configuración del Dataset

El  dataset  consolidado  contiene 10,374,544  registros provenientes  de  2,872  acciones  del

NYSE, distribuidos temporalmente según el protocolo establecido:

15

Aprendizaje Estadístico

Proyecto Semestral

Variables predictoras (13 features técnicos):

•  Retornos: ret_cc_1, ret_oo_1, ret_co_1 (retornos

close-to-close,

open-to-open,

close-to-open de 1 día)

•  Tendencia: sma_5, sma_10, ema_10 (medias móviles simple y exponencial)

•  Momentum: mom_5 (diferencia de precio en 5 días)

•  Volatilidad: std_5, std_10 (desviación estándar de retornos)

•  Rango: range_rel (rango normalizado High-Low/Close)

•  Volumen: vol_ma_10, vol_rel (media móvil y volumen relativo)

•  Temporal: dow (día de la semana, 0=Lunes, 4=Viernes)

Variable objetivo:

Clasificación binaria que indica si la apertura del día siguiente será mayor que el cierre del

día actual (gap overnight).

16

Aprendizaje Estadístico

Proyecto Semestral

17

Aprendizaje Estadístico

Proyecto Semestral

18

Aprendizaje Estadístico

Proyecto Semestral

19

Aprendizaje Estadístico

Proyecto Semestral

6.  Evaluación

20

Aprendizaje Estadístico

Proyecto Semestral

21

Aprendizaje Estadístico

Proyecto Semestral

22

Aprendizaje Estadístico

Proyecto Semestral

Bibliografía

Fama, E. (1969). Efficient Capital Markets: A Review of Theory and Empirical Work. The

Journal of Finance, 383–417.

Gu,  S.,  Kelly,  B.,  &  Xiu,  D.  (2020).  Empirical Asset  Pricing  via  Machine  Learning.  The

Review of Financial Studies, 2223–2273.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning: Data

Mining, Inference, and Prediction. Springer.

Hyndman, R., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice. OTexts.

Mireles Vázquez,  I. (2011). Bolsa de Valores "¿Cómo? ¿Por qué? Y ¿Para qué?".  Tiempo

Económico, 56.

Reyna, A.  (2024).  ¿Qué  es  la  bolsa  de  valores?  Una  explicación  simple.  Retrieved  from

BBVA:  https://www.bbva.com/es/salud-financiera/que-es-la-bolsa-de-valores-una-

explicacion-simple/

Villanueva  Gonzales, A.  (2007).  Mercados  financieros:  una  aproximación  a  la  Bolsa  de

Valores de Lima. Contabilidad y Negocios, 23-33.

23

