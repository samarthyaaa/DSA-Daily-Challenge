class solutions:
  def Maxones(self,nums):
    max=0
    count=0
    for i in nums:
      if i==1:
        count+=1
      else:
        count=0
    if count>max:
      max=count
    return max
nums=[1,0,1,1,1]
s=solutions()
print(s.Maxones(nums))
