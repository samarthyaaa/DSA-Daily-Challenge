Brute:
class Solution:
    def minSubArrayLen(self,target,arr):
        n=len(arr)
        ans=float('inf')

        for i in range(n):
            total=0
            for j in range(i,n):
                total+=arr[j]

                if total>=target:
                    ans=min(ans,j-i+1)
                    break

        if ans==float('inf'):
            return 0
        return ans
