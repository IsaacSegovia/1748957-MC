Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def minimo(arr):
	p=arr[0]
	for q in arr:
		if(q<p):
			p=q
			return p

		
>>> def ordenar(arr):
	arrsort=[]
	for p in range(len(arr)):
		q=minimo(arr)
		arr.remove(q)
		arrsort.append(q)
	return arrsort

>>> import random
>>> r=random.sample(range(2,102),2)
>>> cnt=0
>>> print(r)
[50, 75]
>>> print(r[minimo(r)])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(r[minimo(r)])
TypeError: list indices must be integers or slices, not NoneType
>>> r=random.sample(range(2,102),100)
>>> r
[22, 66, 60, 5, 40, 7, 8, 32, 71, 78, 34, 46, 51, 55, 87, 49, 69, 41, 82, 59, 42, 73, 45, 80, 2, 57, 28, 83, 90, 89, 31, 67, 47, 9, 14, 39, 94, 15, 4, 70, 61, 26, 13, 37, 62, 100, 27, 16, 48, 63, 77, 95, 17, 56, 88, 92, 30, 33, 58, 50, 65, 25, 36, 43, 23, 91, 96, 54, 101, 20, 86, 35, 38, 11, 24, 64, 76, 75, 52, 99, 29, 10, 74, 3, 81, 18, 85, 97, 44, 6, 84, 19, 53, 93, 68, 12, 79, 72, 21, 98]
>>> r=random.sample(range(2,102),2)
>>> r
[37, 68]
>>> print(min(r))
37
>>> print(ordenamientobruto(r))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(ordenamientobruto(r))
NameError: name 'ordenamientobruto' is not defined
>>> print(cnt)
0
>>> 
