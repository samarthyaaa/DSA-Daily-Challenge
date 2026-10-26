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
        left,right=0,len(nums)-1
        while left < right:
            total= nums[left]+ nums[right]
            if total==target:
                return[left,right] 
            elif total>target:
                right= right-1
            else:
                left= left+1
        return []
nums=[2,7,11,15]
target=9
s=Solution()
print(s.twoSum(nums,target))
