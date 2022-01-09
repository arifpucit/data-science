# This is a Python module containing functions. Must have an extension .py
AUTHOR = 'Arif Butt'
BATCH = 2021

#################      Factorial           #########################
def myfactorial(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial





################      Linear Search         ##########################
def myindex(numbers, no):
    for i in range(len(numbers)):  
        if numbers[i] == no:
            return i
    return -1



################      Selection Sort        ##########################
def mysort(numbers, inplace=False):
    n = len(numbers)
    if(inplace == True):
        for i in range(0,n,1):
            min_idx = i
            for j in range(i+1, n):
                if numbers[min_idx] > numbers[j]:
                    min_idx = j
            # Swap the found minimum element with the first element        
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        return None
    else:
        mylist = numbers[:]
        for i in range(0, n, 1):
            min_idx = i
            for j in range(i+1, n):
                if mylist[min_idx] > mylist[j]:#issue
                    min_idx = j
            # Swap the found minimum element with the first element        
            mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
        return mylist
        
        
        
