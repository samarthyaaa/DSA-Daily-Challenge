Brute force:
class Solutions:
  def repeat(self,nums):
    n=len(nums)
    for i in range(n):
      count=0
      for j in range(n):
        if nums[i]==nums[j]:
          count+=1
      if count==1:
        return nums[i]
    return -1
nums=[2,8,3,2,3,8,7]
s=Solutions()
print(s.repeat(nums))
Time Complexity: O(n**2)

Optimal Solution:
class Solutions:
  def repeat(self,nums):
    freq={}
    for i in nums:
      if i in freq:
        freq[i]+=1
      else:
        freq[i]=1
    for i in nums:
      if freq[i]==1:
        return i
    return -1
nums=[2,8,3,2,3,8,7]
s=Solutions()
print(s.repeat(nums))
time complexity :O(n)
