class Solutions:
  def Find_Max(self,nums):
    max=nums[0]
    for i in nums:
      if i>max:
        max=i
    return max
time complexity:O(n)
nums=[4,8,6,33]
s=Solutions()
print(s.findsecmax(nums))
