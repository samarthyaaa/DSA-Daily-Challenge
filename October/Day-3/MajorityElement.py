brute force:
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i]==nums[j]:
                    count+=1
            if count > n//2:
                return nums[i]
        return -1
time complexity: O(n**2)

Optimal solution:
class Solution(object):
    def majorityElement(self, nums):
      count=0
      num=0
      for i in range(len(nums)):
        if count==0:
          num=nums[i]
        if nums[i]==num:
          count+=1
        else:
          count-=1
      return num    
time compexity : O(n)
