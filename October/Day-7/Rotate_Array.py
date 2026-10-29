class solutions:
  def rotate(self,nums,k):
    ans=[]
    n=len(nums)
    k=k%n
    i=n-k
    while i<n:
      ans.append(nusm[i])
      i+=1
    i=0
    while i=n-k:
      ans.append(nums[i])
      i+=1
    i=0
    while i<n:
      nums[i]=ans[i]
      i+=1
Time Complexity: O(n)
