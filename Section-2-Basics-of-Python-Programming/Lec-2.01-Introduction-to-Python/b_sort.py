# Bubble Sort
arr = [25, 15, -6, 8, 2]
n = len(arr)
for i in range(0,n-1,1):
        for j in range(0, n-i-1,1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]                
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])