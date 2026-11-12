Brute:
class Solution:
    def sortBins(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
Optimal:
class Solution:
    def sortBins(self,arr):
        if len(arr)==0:
            return arr
        mini=min(arr)
        maxi=max(arr)
        count=[0]*(maxi-mini+1)
      
        for i in arr:
            count[i-mini]+=1

        ans=[]
        for i in range(len(count)):
            for j in range(count[i]):
                ans.append(i+mini)
        return ans
