Recursive Fibonacci Series
################################################
# Recursive Function for nth Fibonacci number
def recursive_fibo(n):
    if n < 1:
        return -1
    elif n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return recursive_fibo(n-1) + recursive_fibo(n-2)
#################################################
# Driver code
count = 10
print("Fibonacci Series: ", end=' ')
for i in range(1,count,1):
    rv = recursive_fibo(i)
    print(rv, end=' ')


