class solutions:
  def running_sum(self,nums):
    arr=[]
    total=0
    n=len(nums)
    for i in range(n):
      total=total+nums[i]
      arr.append(total)
    return arr
nums=[12,3,4]
s=solutions()
print(s.running_sum(nums))
# Time complexity: O(n))
