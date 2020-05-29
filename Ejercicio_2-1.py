
print("Ejercicio Número 2")
print("Ingresa un número")
numero=int(input())
suma=0
Realizado=True
if(numero<=10000 and numero>0):
   for x in range(1,numero+1):
    	suma=suma+x
elif(numero==0):
  print("Ingrese otro valor")
  exit()

else:
 Realizado=False
 if(numero>=-10000 and numero<0):
     for x in range (-1,numero-1,-1):
         suma=suma+x

if(Realizado==True):
    print("La suma desde 1 hasta " + str(numero)+ " es "+str(suma))
else:
    print("La suma desde -1 hasta " + str(numero)+ " es "+str(suma+1))