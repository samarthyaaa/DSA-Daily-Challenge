class Solutions:
  def maxavg(self,nums,k):
    winsum=0
    for i in range(k):
      winsum+=nums[i]
    maxsum=winsum
    for i in range(k,len(nums)):
      winsum=winsum-nums[i-k]+nums[i]
      maxsum=max(winsum,maxsum)
    return maxsum
nums=[2,1,5,1,3,2]    
s=Solutions()
print(s.maxavg(nums,3))
time complexity: O(n)
