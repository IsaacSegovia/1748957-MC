cnt=0
def fibo(n):
    global cnt
    cnt+=1
    if n==0 or n==1:
        return 1
    return fibo(n-2)+fibo(n-1)
    print('El cnt es:',cnt)
    
cnt=0
def fibo(n):
    global cnt
    if n==0 or n==1:
        return 1
    r, r1, r2=0, 1, 1
    for i in range(2, n):
        cnt+=1
        r=r1+r2
        r2=r1
        r1=r
    return r


memo={}
cnt=0
def fibonacci(n):
    global memo,cnt
    cnt+=1
    if n==0 or n==1:
        return (1)
    if n in memo:
        return memo[n]
    else:
        val=fibonacci(n-2)+fibonacci(n-1)
        memo[n]=val
        return val
