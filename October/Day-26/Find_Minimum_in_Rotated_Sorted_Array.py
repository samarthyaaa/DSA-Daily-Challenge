Brute Force:
class Solution(object):
    def findMin(self, nums):
        min=nums[0]

        for i in nums:
            if i < min:
                min=i
        return min
time complexity:O(n)
Optimal Solution:
class Solutions:
  def minimum(self,nums):
    left,right=0,len(nums)-1
    while left <= right:
      mid=left+(right-left)//2
      if nums[mid] > nums[right]:
        left=mid+1
      else:
        right= mid
  return nums[left]
