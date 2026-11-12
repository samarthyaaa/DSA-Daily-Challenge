Brute:
class Solution:
    def earliestSlot(self,arr,target):
        for i in range(len(arr)):
            if arr[i]>=target:
                return i
        return -1
Optimal:
class Solution:
    def earliestSlot(self,arr,target):
        low=0
        high=len(arr)

        while low<high:
            mid=(low+high)//2

            if arr[mid]<target:
                low=mid+1
            else:
                high=mid

        if low==len(arr):
            return -1

        return low
