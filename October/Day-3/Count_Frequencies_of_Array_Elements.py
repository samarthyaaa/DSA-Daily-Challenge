Brute Force:

class Solutions:
  def repeat(self,nums):
    freq={}
    for i in nums:
      if i in freq:
        freq[i]+=1
      else:
        freq[i]=1
    return freq
nums=[2,8,3,2,3,8,8,7]
s=Solutions()
print(s.repeat(nums))
time complexity: O(n)
