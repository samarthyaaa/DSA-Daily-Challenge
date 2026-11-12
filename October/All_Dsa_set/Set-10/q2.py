Brute:
class Solution:
    def getFloorAndCeil(self,arr,x):
        floor=-1
        ceil=-1

        for i in arr:
            if i<=x:
                floor=i

            if i>=x and ceil==-1:
                ceil=i

        return [floor,ceil]
Optimal:
class Solution:
    def getFloorAndCeil(self,arr,x):
        low=0
        high=len(arr)-1
        floor=-1
        ceil=-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==x:
                return [x,x]

            elif arr[mid]<x:
                floor=arr[mid]
                low=mid+1

            else:
                ceil=arr[mid]
                high=mid-1

        return [floor,ceil]
