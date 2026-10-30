class Solutions:
  def maxavg(self,nums,k):
    winsum=0
    for i in range(k): # calculates the sum
      winsum+=nums[i]
    maxsum=winsum
    for i in range(k,len(nums)):# slides the window
      winsum=winsum-nums[i-k]+nums[i]
      maxsum=max(winsum,maxsum)
    return float(maxsum/k)


    
