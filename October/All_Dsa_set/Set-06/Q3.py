Brute:
class Solution:
    def combine(self,a,b):
        arr=a+b
        n=len(arr)

        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
Optimal:
class Solution:
    def combine(self,a,b):
        i=0
        j=0
        ans=[]
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                ans.append(a[i])
                i+=1
            else:
                ans.append(b[j])
                j+=1
        while i<len(a):
            ans.append(a[i])
            i+=1

        while j<len(b):
            ans.append(b[j])
            j+=1

        return ans
