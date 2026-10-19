class Solution:
    def quickSort(self, arr):
        if len(arr) <= 1: # Stop if the list has 0 or 1 element
            return arr

        pivot = arr[0] # Choose the first element as pivot
        left = []
        right = []
        for i in range(1, len(arr)):# Separate elements around the pivot
            if arr[i] <= pivot:
                left.append(arr[i])  
            else:
                right.append(arr[i]) 

        return self.quickSort(left) + [pivot] + self.quickSort(right)
