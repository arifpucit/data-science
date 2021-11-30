# Insertion Sort
arr = [25, 15, -6, 9, 2]
n = len(arr)
for i in range(1, n):
    key = arr[i] #extraction
    j = i -1
    while j >=0 and key < arr[j] :
        arr[j+1] = arr[j] #right shift
        j = j - 1
    arr[j+1] = key  #insertion
 
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])