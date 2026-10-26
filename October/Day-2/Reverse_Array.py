class Solutions:
  def FindSecMax(self,nums):
    l,h=0,len(nums)-1
    while l<h:
      nums[l],nums[h]=nums[h],nums[l]
      l+=1
      h-=1
    return nums
nums=[8,22,36,8]
s=Solutions()
print(s.FindSecMax(nums))

time complexity=O(n)
