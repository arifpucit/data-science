# Selection Sort
arr = [25, 15, -6, 8, 2]
n = len(arr)
for i in range(0,n,1):
    min_idx = i
    for j in range(i+1, n):
                   if arr[min_idx] > arr[j]:
                        min_idx = j
    # Swap the found minimum element with the first element        
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])