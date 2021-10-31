# Iterative Linearly search
# If x is present then return its index else return -1
######################################
def l_search_iterative(arr, no):
    for i in range(len(arr)):  
        if arr[i] == no:
            return i
    return -1
######################################
 
# Driver code
arr = [5, 3, 8, 2, 1]
no = 8
rv = l_search_iterative(arr, no)
if rv == -1:
    print("Not found")
else:
    print("Found at index %d" %rv)