class Solution(object):
    def mySqrt(self, x):
        lo, hi=0,x
        while lo <= hi:                      
            mid = lo + (hi - lo) // 2        
            if mid * mid == x:
                return mid
            if mid*mid < x:
                lo = mid + 1               
            else:
                hi = mid - 1   
        return hi  
