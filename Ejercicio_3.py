print("Ingresa tus números")
aux=False
aux2=False
posiciones=[]
conti=0
while aux==False:
    n=int(input())
    if(n>=1 and n<=1500):
        posiciones.append(n)
    elif(n==0 and conti==0 or n>1500 and conti==0):
        exit()
    elif(n==0 and conti>0):
       aux=True
    conti=conti+1

feos=[1]  
z=2   
act=z    
pos=2  

while pos<=max(posiciones):
    while(z % 2==0):
       z=z/2
    while(z % 3==0):
       z=z/3
    while(z%5==0):
       z=z/5
    if(z==1):
       feos.append(act)
       pos=pos+1 
    act=act+1
    z=act

print("A continuacion se mostrará la lista de números feos:")
print(feos)
print("Los numeros elegidos son:")
for x in range(0,len(posiciones)):
    pos=posiciones[x]
    print(feos[pos-1])
