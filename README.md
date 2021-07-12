# calcula_aplicativos
Scripts para calcular importes y número de registros de percepciones y retenciones de distintos aplicativos (ARBA, DREI, SIAGER, SICORE, SIRCAR).

En el caso de [aplicativos_quincenales](https://github.com/akalautaro/calcula_aplicativos/blob/main/aplicativos_quincenales.py) los parámetros que hay que pasarle son:
* --mes
* --quincena
* --loter (para retenciones ARBA)

#### Ejemplo: ./calcula_aplicativos_gh/aplicativos_mensuales.py --mes 6 --anio 2021 --lotep 135 --jur 914

Para _[aplicativos_mensuales]_(https://github.com/akalautaro/calcula_aplicativos/blob/main/aplicativos_mensuales.py):
* --mes
* --anio
* --lotep (para percepciones ARBA)
* --jur (jurisdicción para sircar)

#### Ejemplo: ./calcula_aplicativos_gh/aplicativos_quincenales.py --mes 6 --quincena 2

Por cuestiones de privacidad, en la carpeta aplicativos se encuentran archivos de prueba con datos ficticios para probar los scripts. En los aplicativos_mensuales la función para procesar el archivo correspondiente al SIAGER está comentada, ya que no subí ningún archivo de prueba para este aplicativo. Los resultados se guardan en diferentes archivos con número de registros y el importe total, alojados en la carpeta resultados.
