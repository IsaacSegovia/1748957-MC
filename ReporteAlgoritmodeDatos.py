import random
cnt=0
def arregolosgenerados(cantidaddearreglos):
	n=cantidaddearreglos
	for i in range(1, n+1):
		arri=random.sample(range(1,10000),10+5*(i-1))
		selection(arri)
		quicksort(arr)
		orden_por_insercion(arri)
		bubble(arri)

def selection(arr):
	global cnt
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[val]:
				val=j
				cnt+=1
		if val!=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	print(cnt)	


def quicksort(arr):
	global cnt
	if len(arr) <= 1:
		return arr
	p=arr.pop(0)
	menores, mayores=[], []
	for e in arr:
		cnt+=1 
		if e <=p:
			menores.append(e)
		else:
			mayores.append(e)
	print(cnt)

def orden_por_insercion(array):
    global cnt
    for indice in range (1,len(array)):
        valor=array[indice]
        i=indice-1
        while i>=0:
            cnt+=1
            if valor<array[i]:
                array[i+1]=array[i]
                array[i]=valor
                i-=1
            else:
                break
    print(cnt)
	
