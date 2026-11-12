Brute:
class Solution:
    def firstBadVersion(self,n):
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
        return -1
Optimal:
class Solution:
    def firstBadVersion(self,n):
        low=1
        high=n

        while low<high:
            mid=(low+high)//2

            if isBadVersion(mid):
                high=mid
            else:
                low=mid+1

        return low
