#Insercion

def orden_por_insercion(array):
	global cnt
	for indice in range (1, len(array)):
		valor=array[indice] #valor es el elemento que vamos a comparar
		i=indice-1          #i es el valor anterior al elemento que estamos comparando
		while i>=0:
			cnt=cnt+1
			if valor<array[i]:  #comparamos valor con el elemtno anterior
				array[i+1]=array[i]  #Intercambiamos los valores
				array[i]=valor
				i-=1 #Decrementamos en 1 el valor de i
			else:
				break
	return array
A=[26,2,45,30,1,450,1]
cnt=0
orden_por_insercion(A)