# Merge Sort

def merge(arr, l, m, r):
    n1 = m - l + 1 #length of left array
    n2 = r - m     #length of right array
 
    # create two temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy left half data of arr inside array L
    for i in range(0, n1):
        L[i] = arr[l + i]
    # Copy right half data of arr inside array R
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of L
    j = 0     # Initial index of R
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
        k = k+1
 
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i = i+1
        k = k+1
 
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j = j+1
        k = k+1
 
 
######################################
def MS(arr, l, r):
    if l < r:
        m = (l+r)//2
        MS(arr, l, m)
        MS(arr, m+1, r)
        merge(arr, l, m, r)
######################################
 
# Driver code
arr = [5, 3, 8, 2, 1]
n = len(arr)
MS(arr, 0, n-1)
print("Sorted array is")
for i in range(n):
    print(arr[i])