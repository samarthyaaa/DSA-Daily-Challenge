Brute:
class Solution:
    def searchInsert(self,arr,target):
        for i in range(len(arr)):
            if arr[i]>=target:
                return i
        return len(arr)
Optimal:
class Solution:
    def searchInsert(self,arr,target):
        low=0
        high=len(arr)

        while low<high:
            mid=(low+high)//2

            if arr[mid]<target:
                low=mid+1
            else:
                high=mid

        return low
