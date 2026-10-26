class Solutions:
  def findsecmax(self,nums):
    max=float('-inf')
    sec=float('-inf')
    for i in nums:
      if i>max:
        sec=max
        max=i
      elif i< max and i> sec:
        sec=i
    if sec==float('-inf'):
      return -1
    return sec

#time complexity : O(n)
    
nums=[4,8,6,33]
s=Solutions()
print(s.findsecmax(nums))
