# Recursive Linear search
# If x is present then return its index else return -1
######################################
def l_search_recursive(arr, l, r, no):
    if r < l:
        return -1
    if arr[l] == no:
        return l
    if arr[r] == no:
        return r
    return l_search_recursive(arr, l+1, r-1, no)
######################################
 
# Driver code
arr = [5, 3, 8, 2, 1]
n = len(arr)
no = 6
rv = l_search_recursive(arr, 0, n-1, no)
if rv == -1:
    print("Not found")
else:
    print("Found at index %d" %rv)

