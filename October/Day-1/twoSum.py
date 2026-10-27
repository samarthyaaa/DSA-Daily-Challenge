Brute force:

class Solutions()
def twoSum(self,nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            total=nums[i]+nums[j]
            if total==target:
                return[i,j]
        return []
nums=[2,7,11,3]
target=9
s=Solutions()
print(s.twoSum(nums,target))

Time Complexity=O(n**2)

Optimal method:
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i

nums=[2,7,11,15]
target=9
s=Solution()
print(s.twoSum(nums,target))
