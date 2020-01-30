# Calculadora de números imaginarios 

Libreria la cual es capaz de hacer operaciones básicas de números complejos representados como tuplas. 
Sus operaciones incluyen: suma, resta, multiplicación, división, modulo, conjugado, cambio de coordenadas cartesianas a polares y retornar la fase del complejo.

## Comenzando 

Se empieza con la idea de que las operaciones tales como la suma y la resta de los numeros complejos es la misma que una suma de vectores, pero al llegar a la multiplicacion y division de numeros complejos se tiene que tener en cuenta la respectiva formula para que nos de el resultado correspondiente.

Para hacer la funcion conjugado, se tiene que saber que esta operacion significa dejar el numero imaginario como negativo.

Para las siguientes funciones se tiene primero que importar la biblioteca math, la cual nos ayuda con las funciones tales como la funcion seno, coseno, raiz entre otras mas.

Para la funcion modulo se necesita de la funcion raiz para poder hallar el resultado correspondiente.

Para la funcion retorno de fase se necesita de la funcion tangente^-1 para poder hallar el angulo que se requiere, el cual es el resultado total.

Para la funcion pasar de coordenadas cartesianas a polares se necesita la funcion raiz, con la cual encontramos la longitud de la recta polar, asi como tambien necesitamos la funcion tangente^-1 para hallar el angulo correspondiente. Estos dos valores encontrados forman una tupla la cual concluye el paso de coordenadas.

## Ejecucion de pruebas
Para la ejecucion de las pruebas automarizadas creadas para el programa de calculadora, se hizo un programa con el nombre de test.py con su respectivo codigo para las operaciones que se requieran probar con otros numeros.

### Analisis de pruebas
La funcionalidad que se le da a las pruebas es poder concluir que las ocho operaciones creadas en el programa expuesto funcionen con cualquier tupla de valores, sin importar si son tuplas de numeros enteros o con decimales de maximo dos cifras.

### Codigo de pruebas
test_suma = Esta prueba tiene como finalidad testear la funcion suma de la calculadora de numeros complejos

test_resta = Esta prueba tiene como finalidad testear la funcion resta de la calculadora de numeros complejos

test_multiplicacion = Esta prueba tiene como finalidad testear la funcion multiplicacion de la calculadora de numeros complejos

test_division = Esta prueba tiene como finalidad testear la funcion division de la calculadora de numeros complejos

test_conjugada = Esta prueba tiene como finalidad testear la funcion conjugado de la calculadora para una tupla de numeros complejos

test_fase = Esta prueba tiene como finalidad testear la funcion retorno en una tupla de numeros.

test_modulo = Esta prueba tiene como finalidad testear la funcion modular en una tupla de numeros

test_polar = Esta prueba tiene como finalidad testear la funcion que pasa de coordenadas cartesianas a polares una tupla de numeros

## Construido con :

* [Python](https://www.python.org/) - Lenguaje de programacion


## Autores ✒

* Juan Carlos Baez Lizarazo 

