# calcula_aplicativos
Scripts para calcular importes y número de registros de percepciones y retenciones de distintos aplicativos (ARBA, DREI, SIAGER, SICORE, SIRCAR).

En el caso de _[aplicativos_quincenales]_(https://github.com/akalautaro/calcula_aplicativos/blob/main/aplicativos_quincenales.py) los parámetros que hay que pasarle son:
* --mes
* --quincena
* --loter (para retenciones ARBA)

Para _[aplicativos_mensuales]_(https://github.com/akalautaro/calcula_aplicativos/blob/main/aplicativos_mensuales.py):
* --mes
* --anio
* --lotep (para percepciones ARBA)
* --jur (jurisdicción para sircar)

Por cuestiones de privacidad, en la carpeta aplicativos se encuentran archivos de prueba con datos ficticios para probar los scripts. En los aplicativos_mensuales la función para procesar el archivo correspondiente al SIAGER está comentada, ya que no subí ningún archivo de prueba para este aplicativo. Los resultados se guardan en diferentes archivos con número de registros y el importe total, alojados en la carpeta resultados.
