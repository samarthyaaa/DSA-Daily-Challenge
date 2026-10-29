class Solutions:
  def rotate(self,nums,k):
    n=len(nums)
    if n==0:
      return nums
    k=k%n
    i=0
    j=n-1
    while i<j:
      nums[i],nums[j]=nums[j],nums[i]
      i+=1
      j-=1
    i=0
    j=k-1
    while i <j:
      nums[i],nums[j]=nums[j],nums[i]
      i+=1
      j-=1
    i=k
    j=n-1
    while i<j:
      nums[i],nums[j]=nums[j],nums[i]
      i+=1
      j-=1
