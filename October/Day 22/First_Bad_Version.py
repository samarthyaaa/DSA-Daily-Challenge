Brute Force:
class Solution:
    def firstBadVersion(self, n):
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i
Optimal Solution:                
class Solution(object):
    def firstBadVersion(self, n):
        lo=1
        hi=n
        while lo<hi:
            mid=lo+(hi-lo)//2
            if isBadVersion(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
