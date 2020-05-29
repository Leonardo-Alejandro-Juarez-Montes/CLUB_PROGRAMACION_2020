import math
print("Ingresa el numero de datos a ingresar")
turno=int(input())
NoPuntos=[]
print(" ")
for x in range(0,turno):
     n=int(input())
     NoPuntos.append(n)
for y in range(0,turno):
     z=NoPuntos[y]
     part1=pow(z,4)/24
     part2=pow(z,3)/4
     part3=23*pow(z,2)/24
     part4=(3*z)/4
     print("Valor posicion "+str(y)+ " : " +str(math.floor(part1-part2+part3-part4+1)))
 
