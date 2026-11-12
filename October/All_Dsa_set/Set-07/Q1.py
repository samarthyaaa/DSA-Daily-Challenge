Brute:
class Solution:
    def search(self,arr,target):
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return -1
Optimal:
class Solution:
    def search(self,arr,target):
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return -1
