class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        left=0
        seen=set()
        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            if right-left>=k:
                seen.remove(nums[left])
                left+=1
        return False
        
