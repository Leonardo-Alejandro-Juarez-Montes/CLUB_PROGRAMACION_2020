ingresado=0
resultados=[]
while(ingresado!=-1):
	suma=0
	ingresado=int(input())
	if(ingresado==-1):
		break
	for x in range(1,ingresado):
		if(ingresado%x==0):
			suma+=x
	if(suma==ingresado):
		resultados.append(True)
	else:
		resultados.append(False)			
	
for x in range(0,len(resultados)):
	if(resultados[x]==True):
		print("Número perfecto")
	else:
		print("Número no perfecto")

		