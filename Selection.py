#Selection
def selection(arr):
	for i in range(0,len(arr)-1):
		val=1
		for j in range(i+1,len(arr)):
			if arr[j]<arr[val]:
				val=j
		if val !=i:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr

#Probar 
import random

def ran_n(n,lim_i=0_s=100):
	arr=[]
	for i in range(n):
		arr.append(random. randint(lim_i,lim_s))
	return arr
