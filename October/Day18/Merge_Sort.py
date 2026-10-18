
class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2

            self.mergeSort(arr, l, mid) # Dividing the array into two halfs
            self.mergeSort(arr, mid + 1, r)

            left = arr[l:mid + 1]
            right = arr[mid + 1:r + 1]

            i = j = 0
            k = l

            while i < len(left) and j < len(right): # Compare elements from both the halfs
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left): # Copy remaining left elements
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right): # Copy remaining right elements
                arr[k] = right[j]
                j += 1
                k += 1
