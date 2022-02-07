def fibo(n):
    if n<=1:
        return n
    else:
        #print(fibo(n-1))
        #print(fibo(n-2))
        return (fibo(n-1)+fibo(n-2))

n = int(input("Enter the term"))
print(fibo(n))