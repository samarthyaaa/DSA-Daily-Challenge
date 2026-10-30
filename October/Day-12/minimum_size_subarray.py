class Solution:
    def minSubArrayLen(self, target, nums):
        left=0
        winsum=0
        minlen=float('inf')
        for right in range(len(nums)):
            winsum+=nums[right]
            while winsum>=target:
                length = right - left +1
                minlen=min(minlen,length)
                winsum-=nums[left]
                left+=1
        if minlen==float('inf'):
            return 0
        return minlen
