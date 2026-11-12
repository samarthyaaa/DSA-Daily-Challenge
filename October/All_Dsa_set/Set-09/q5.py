Brute:
class Solution:
    def insert(self,intervals,newInterval):
        arr=intervals+[newInterval]
        n=len(arr)

        for i in range(n):
            for j in range(n-1-i):
                if arr[j][0]>arr[j+1][0]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        ans=[]

        for i in arr:
            if not ans or i[0]>ans[-1][1]:
                ans.append(i[:])
            else:
                ans[-1][1]=max(ans[-1][1],i[1])

        return ans
