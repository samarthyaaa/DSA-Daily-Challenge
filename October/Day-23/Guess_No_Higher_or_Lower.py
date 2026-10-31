for i in range(1, n + 1):
    result = guess(i)
    if result == 0:
        return i
Optimal solution:
class Solution(object):
    def guessNumber(self, n):
        low,high=1,n
        while low <= high:
            mid=low+(high-low)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high=mid-1
            else:
               low=mid+1
        return high
        
