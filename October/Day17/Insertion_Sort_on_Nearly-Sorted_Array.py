class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            j = i

               while j > 0 and arr[j - 1] > arr[j]: # Move elements to their correct positions
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # Swap elements if in the wrong order
                j -= 1
        return arr
