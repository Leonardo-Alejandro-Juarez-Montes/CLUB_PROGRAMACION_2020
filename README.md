# CLUB_PROGRAMACION_2020
Juárez Montes Leonardo Alejandro No.Control: 19161312

Este es mi repositorio, el cual contiene los ejercicios realizados en el transcurso del Club de programación.
A continuacion muestro una breve explicacion de lo que se hizo para resolver cada UNO.

EJERCICIO 1

El ejercicio nos pide ingresar dos nmumeros en una sola linea los cuales deben estar separados por un espacio para posteriormente realizar
la suma de ambos e imprimirla.
1.-Se utilizo el método "split" el cual nos permite convertir una cadena de texto en un arreglo(ingresara en una posicion distinta 
cada palabra o elemento separado por un espacio).
2.-Ya obtenido el arreglo,procedemos a guardar los valores almacenados en dos variables distintas y posteriormente las sumamos e imprimimos. 

EJERCICIO 2 

El ejercicio nos pide realizar una suma desde 1 hasta cierto número "n" ya sea positivo o negativo(0<n<10000 y 0>n>-10000)
1.-Para realizar la suma se hace uso de un ciclo que va desde uno hasta el numero n en el cual se iran acumulando todos sus numeros antecesores.
2.- Lo mismo aplica para un numero negativo solo que en vez de hacer un recorrido positivo por el ciclo se hace de forma negativa hasta llegar a -n.
4.- Posterirmente se imprime la sumatoria.

EJERCICIO 3 

Los numeros feos son todos aquellos numeros que son multiples de 2 o 3 o 5.
El ejercicio nos pide imprimir las ingresar cada posicion de un numero feo en lineas diferentes y posteriormente imprimirlas.
1.-Almacenamos cada posicion ingresada en un arreglo.
2.- Obtenemos la posicion más grande del arreglo "n".
3.- Ahora procedemos a generar los numeros feos hasta la n posición.
4.- Se hizo uso de un ciclo while para generar cada numero feo hasta la posición n.
5.-Dentro del ciclo mencionado generamos otros 3 ciclos los cuales nos ayudaran a obtener el numero feo, esos ciclos dividiran una cantidad
entre 2,3 o 5, y si la cantidad es divisible entre cualquiera de esos 3 numeros el valor se guarda en un arreglo.
6.- Al final se imprimen las posiciones del arreglo las cuales fueron especificadas al principio.

EJERCICIO 4

Este ejercicio nos pide calcular el numero de areas en que se divide un circulo despues de trazar todas las rectas que pasan por n puntos.
 1.- Para ello ingresamos el numero de puntos
 2.- Utilizamos una formula la cual contiene potencias(se utiliza el metodo pow)
 3.- Para agilizar se dividio la operacion en partes, 
 4.-Al final solo se imprime la suma de todas las operaciones individuales.
 
 EJERCICIO 5 
 Este ejercicio se basa en obtener numeros perfectos aquellos cuya suma de sus divisores da el mismo numero.
 1.- Hacemos un ciclo que abarque desde 1 hasta el numero n.
 2.- DIvidimos el numero en entre cada valor que tome el ciclo y si obtenemos como residuo 0, agregamos el vqlor del ciclo en la variable suma.
 3.- Al term,inar con el ciclo comparamos el valor de la suma con el numero ingresado y si son iguales, el numero ingresado es perfecto.
