class Solutions:
  def pivot_Index(self,nums):
    left_sum=0
    total=sum(nums)
    n=len(nums)
    i=o
    while i < n:
      right=total-left-nums[i]
      if right==left_sum:
        return i
      left_sum=left_sum+nums[i]
      i+=1
    return -1
      
    
    
