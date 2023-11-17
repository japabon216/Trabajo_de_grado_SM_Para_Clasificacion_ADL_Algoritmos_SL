# Trabajo_de_grado_SM_Para_Clasificacion_ADL_Algoritmos_SL

En el presento proyecto se pueden encontrar diferentes archivos que describen un proyecto de ciencia de datos realizado con el fin de obtener de Stream Learning que clasifique actividades de la vida diaria, adicionalmente también se contribuye con una comparación de algoritmos de Stream y Batch Learning en el contexto de clasificación de ADL o HAR, finalmente también se contribuye con el despliegue del clasificar con una primera versión del aplicativo móvil Jaida. Para realizar estas contribuciones se desarrollaron diferentes códigos presentados en este repositorio, donde:

Los cuadernos de colab Parte_1 a Parte_13 realizan las siguientes funciones:

-> Parte_1, Parte_2 y Parte_3 describen la estructuración, limpieza y en general la preparación de cada uno de los datasets encontrados, donde los datos de cada uno de los mismos se estructuraron de tal manera que toda la información proporcionada quede en el mismo formato con la misma cantidad de columnas. Finalizada la estructuración se realizó un proceso de remuestreo de frecuencia con el cual se llevó a todos los datasets a la frecuencia de 50 Hz y se llevaron a las mismas unidades los sensores de giroscopio y acelerómetro.

-> Parte_4 se presenta el mapeo de las actividades en cada uno de los datasets, así como consideraciones adicionales que tuvieron los mismos como cambios en las unidades y eliminación de valores atípicos. Finalmente, la unión de todos los datasets en un dataset denominado dataset unificado, este dataset pasó a una depuración adicional, este dataset se denomina dataset unificado depurado.

-> Parte_5 Presenta el proceso para la extracción de características, donde primero se normalizó el dataset unificado depurado debido a la diferencia de los diferentes rangos en cada uno de los sensores. Hecho esto se segmentó el dataset cada 500 muestras. Con esto, a cada segmento se le calcularon las características pertinentes. Obteniendo un dataset denominado dataset definitivo.

-> Parte_6 Se encuentra la prueba de los algoritmos de Stream y Batch Learning. En este cuaderno se encuentran los diferentes modelos, los resultados y diferentes gráficas pertinente,
En este cuaderno se encuentran los modelos tanto con valores aleatorios como sin valores aleatorios.

-> Parte_7 A diferencia del cuaderno anterior, en este se presenta los modelos depurados, es decir entrenamiento con el dataset sin 16 de únicamente 5 y 7 actividades.

-> Parte_8, Parte_9, Parte_10 y Parte_11 describen la evaluación realizada de los modelos depurados en datasets externos e internos, donde la diferencia recae en que los datasets externos son datasets que no se incluían en el entrenamiento y por lo tanto simulan un entorno 'real', estos datasets son el 9 y 16.

-> Parte_12 presenta la evaluación en todos los datasets tanto externos como internos, pero haciendo uso de la función incremental de Stream Learning.

-> Parte_13 Corresponde a la clasificación de las actividades del dataset 9, tomando filas al azar del mismo y clasificándolas haciendo uso del modelo de 5 actividades de Stream Learning (Modelo usado en el sistema móvil). Adicionalmente se presenta la clasificación haciendo uso de la función incremental de Stream Learning.

En la capeta Sistema_Movil_Jaida se encuentra el backend realizado en flask en proyecto_jaida  y la interfaz de flutter se encuentra en hello_flutter.

En la carpeta Modelos se encuentran los modelos tanto de Stream como de Batch de 5 y 7 actividades.

Finalmente, el sistema móvil se presenta como jaida_app.apk.






