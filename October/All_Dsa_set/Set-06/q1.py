Brute:
class Solution:
    def ranking(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
Optimal:
class Solution:
    def ranking(self,arr):
        count=[0]*101
        for i in arr:
            count[i]+=1

        ans=[]
        for i in range(100,-1,-1):
            for j in range(count[i]):
                ans.append(i)
        return ans
