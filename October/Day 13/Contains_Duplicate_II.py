class Solution(object):
    def checkDuplicate(self, nums, k):
        d={} # stores index
        for i in range(len(nums)): # Check numbers
            if nums[i] in d and i-d[nums[i]] <=k: 
                return True
            d[nums[i]]=i # update index
        return False # no duplicate
