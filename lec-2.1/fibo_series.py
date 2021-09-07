#Iterative Fibonacci Series
def fibo_series(n):
    a=1
    b=1
    print("Fibonacci Series: ", end=' ')
    if n<1:
        print("Incorrect input")
    elif n==1:
        print('0', end=' ')
    elif n==2:
        print('0','1', end=' ')
    else:
        print('0',a,b,end=' ')
        for i in range(n-3):
            c = a + b
            print(c, end=' ')
            a = b  
            b = c
        print()       
         
fibo_series(7)