print("Ingresa tus números")
aux=False
aux2=False
posiciones=[]

while aux==False and aux2==False:
    n=int(input())
    if(n>=1 and n<=1500):
      posiciones.append(n)
    elif(n==0):
       aux=True
       print("Haz ingresado todos los numeros")
    else:
      aux2=True
      print("Números no validos")

feos=[1]
z=2
cont=0
if(aux2==False):
   while cont<=max(posiciones)+1:
     if(z % 2==0 or z % 3==0 or z % 5==0):
        feos.append(z)
     z=z+1
     cont=cont+1   

print("A continuacion se mostrará la lista de números feos:")
print(feos)
print("Los numeros elegidos son:")
for x in range(0,len(posiciones)):
   pos=posiciones[x]
   print(feos[pos-1])


 