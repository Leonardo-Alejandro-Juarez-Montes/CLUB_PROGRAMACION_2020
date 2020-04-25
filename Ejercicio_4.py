print("¿Cuantas veces deseas elegir el numero de puntos?")
turno=int(input())
NoPuntos=[]
print("Indica el numero de puntos que tiene la circunferencia")
print(" ")
for x in range(0,turno):
     print("Turno Número " + str(x+1)+" :")
     n=int(input())
     NoPuntos.append(n)
print(" ")
print("Los resultados respecto al turno son los siguientes")
for y in range(0,turno):
     print("Turno Número " + str(y+1)+" :")
     z=NoPuntos[y]
     resultado= pow(2,z-1)
     print(resultado)
