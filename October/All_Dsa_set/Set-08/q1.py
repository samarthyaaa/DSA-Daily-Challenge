Brute:
class Solution:
    def mySqrt(self,x):
        i=0
        while i*i<=x:
            i+=1
        return i-1
Optimal:
class Solution:
    def mySqrt(self,x):
        low=0
        high=x
        ans=0

        while low<=high:
            mid=(low+high)//2

            if mid*mid<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1

        return ans
