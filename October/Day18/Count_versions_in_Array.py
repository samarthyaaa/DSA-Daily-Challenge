class Solution:
    def count(self, arr):
        if len(arr) <= 1:
            return 0

        mid = len(arr) // 2
        left = [0] * mid
        right = [0] * (len(arr) - mid)
      
        for i in range(mid): # Copy both halfs
            left[i] = arr[i]

        for i in range(len(right)):
            right[i] = arr[mid + i]

        total = self.count(left) + self.count(right)
        i = j = k = 0

        while i < len(left) and j < len(right):   # Merge sorted halfs
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                total += len(left) - i
                j += 1
            k += 1
        while i < len(left):  # Copy remaining elements
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return total
