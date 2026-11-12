Brute:
class Solution:
    def allocateBooks(self,arr,k):
        n=len(arr)

        if k>n:
            return -1
        low=max(arr)
        high=sum(arr)
        for limit in range(low,high+1):
            students=1
            total=0
            for i in arr:
                if total+i>limit:
                    students+=1
                    total=i
                else:
                    total+=i
            if students<=k:
                return limit
        return -1
Optimal:
class Solution:
    def allocateBooks(self,arr,k):
        n=len(arr)

        if k>n:
            return -1

        low=max(arr)
        high=sum(arr)

        while low<high:
            mid=(low+high)//2
            students=1
            total=0

            for i in arr:
                if total+i>mid:
                    students+=1
                    total=i
                else:
                    total+=i

            if students<=k:
                high=mid
            else:
                low=mid+1

        return low
