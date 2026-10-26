Brute force:
class Solutions:
  def single_number(self,nums):
    n=len(nums)
    
    for i in range(n):
        count=0
        for j in range(n):
          if nums[i]==nums[j]:
            count+=1
        if count==1:
          return nums[i]
    return -1
nums=[4,1,2,1,2]       
s=Solutions()
print(s.single_number(nums))
time complexity: O(n**2)

Optimal Solution:
class Solution(object):
    def singleNumber(self, nums):
        ans=0
        for i in nums:
            ans=ans^i
        return ans
timw complexity: O(n)
      
