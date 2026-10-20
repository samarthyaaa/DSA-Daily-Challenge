def binary_search(arr, target):
    lo=0, hi=len(arr) - 1
    while lo <= hi:                     
        mid = lo + (hi - lo) // 2   # divides the search space
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1         
        else:
            hi = mid - 1                
    return -1  # return the index value
