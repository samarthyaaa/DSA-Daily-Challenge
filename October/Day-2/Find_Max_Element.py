class Solutions:
  def Find_Max(self,nums):
    max=nums[0]
    for i in nums:
      if i>max:
        max=i
    return max
time complexity:O(n)
      
