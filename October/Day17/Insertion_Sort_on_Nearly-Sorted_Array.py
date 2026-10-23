def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]      # shift right - no swapping
            j -= 1
        arr[j + 1] = key             # one write, at the end
    return arr
