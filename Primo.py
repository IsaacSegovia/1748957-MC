cnt=0
def pr(num):
    n=num
    a=0
    b='no'
    c='si'
    for i in range(1,n+1):
        if n%i==0:
            a=a+1
    if a!=2:    
        return b
    else:
        return c

for w in range(1,n): #n es cualquier valor que le asigne
	print(w,pr(w))
