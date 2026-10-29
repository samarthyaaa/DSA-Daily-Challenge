class Solutions:
  def reverse(self,nums,k):
    n=len(nums)
    i=0
    while i<n:
      left=i
      right=i+k-1
      if right>=n:
        right=n-1
      while left < right:
      nums[left],nums[right]=nums[right],nums[left]
        i+=1
        j-=1
    i+=k
    
    
      
    
