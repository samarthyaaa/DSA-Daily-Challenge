def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i=i+1
    temp=arr[i]
    arr[i]=arr[high]
    arr[high]=temp

return i
