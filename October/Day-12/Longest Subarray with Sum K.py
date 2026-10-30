class Solution:
  def longsub(self,nums,k):
    maxlen=0
    left=0
    winsum=0
    for right in range(len(nums)):
      winsum+=nums[right]
      while winsum>k:
        winsum-=nums[left]
        left+=1
      if winsum==k:
        length=right-left+1
        maxlen=max(maxlen,length)
    return maxlen
time complexity: O(n)

        
