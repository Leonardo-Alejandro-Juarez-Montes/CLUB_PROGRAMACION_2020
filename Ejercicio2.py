print("Ejercicio Número 2")
print("Ingresa un número")
numero=int(input())
suma=0

if(numero<=10000 and numero>=0):
    for x in range(1,numero+1):
    	suma=suma+x
suma=str(suma)
numero=str(numero)
print("La suma desde 1 hasta " + numero+ " es "+suma)
