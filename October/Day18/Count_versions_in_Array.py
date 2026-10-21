class Solution:
    def MergeSort(self, arr):
        if len(arr) <= 1:
            return 0

        mid = len(arr) // 2
        left = [:mid]
        right = [mid:]
        count=0

        count=count+self.MergeSort(left)
        count=count+self.MergeSort(right)
        i=0
        j=0
        k=0
      
        while i<len(left) and j<len(right):# Copy both halfs
            if left[i] <= right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            arr[k]=left(i)
            i=i+1
            k=k+1
        while j<len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1
        return count
        
            
    
            
            

    
