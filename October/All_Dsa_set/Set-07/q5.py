Brute:
class Solution:
    def search(self,arr,target):
        low=0
        high=len(arr)-1

        while low<high:
            mid=(low+high)//2

            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                high=mid

        peak=low

        low=0
        high=peak

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1

        low=peak+1
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                low=mid+1
            else:
                high=mid-1

        return -1
