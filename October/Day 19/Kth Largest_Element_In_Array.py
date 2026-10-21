class Solution:
    def findKthLargest(self, nums, k):
        low=0
        high=len(arr)-1
        target=len(arr)-k
        while low<=high:
            p=self.partition(arr,low,high)
            if p == target:
                return arr[p]
            elif p < target:
                low=p+1
            else:
                high=p-1

        def partition(self,arr,low, high):
            pivot = nums[high]
            i = low 

            for j in range(low, high):
                if arr[j]<=pivot:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
           temp=arr[j]
           arr[i]=arr[high]
           arr[high]=temp
    return i

