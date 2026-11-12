Brute:
class Solution:
    def twoSum(self,arr,target):
        n=len(arr)

        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==target:
                    return [i,j]

        return []
Optimal:
class Solution:
    def twoSum(self,arr,target):
        left=0
        right=len(arr)-1

        while left<right:
            total=arr[left]+arr[right]

            if total==target:
                return [left,right]
            elif total<target:
                left+=1
            else:
                right-=1

        return []
