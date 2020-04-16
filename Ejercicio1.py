print("Ejercicio Numero 1")
print("Ingresa 2 números, de la siguiente forma")
print("A B")
cadena= input()
space=cadena.index(" ")
A=space
B=space

A=int(cadena[0:space])
B=int(cadena[space:len(cadena)])

if (A>=0 and B<=10):
	suma= A+B
	suma= str(suma)
	print("La suma de ambos números es: " + suma) 
else:
	print("Ingresa otros numeros")
	print("Recuerda 'A' debe ser mayor o igual a 0 y 'B' menor o igual a 10")
