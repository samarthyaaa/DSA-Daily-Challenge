Brute Force:
class solutions:
  def contains_duplicate(self,nums):
    n=lem(nums)
    for i in range(n):
      for j in range(i+1,n):
        if nums[i]==nums[j]:
          return True
    return False
nums=[1,2,3,1]
s=Solutions()
print(s.contains_duplicate(nums))

time complexity: O(n**2)

class Solutions:
  def contains_duplicate(self,nums):
    S=set()
    for i in nums:
      if i in S:
        return True
        S.add(i)
    return False
nums=[1,2,3,1]
s=Solutions()
print(s.contains_dupliacte(nums))

Time complexity = O(n)
