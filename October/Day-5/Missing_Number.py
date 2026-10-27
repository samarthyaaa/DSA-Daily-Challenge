class Solution(object):
    def missingNumber(self, nums):
        seen=set()
        for i in nums:
            seen.add(i)
        for i in range(0,len(nums)+1):
            if i not in seen:
                return i
time complexity: O(n)
            
