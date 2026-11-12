Brute:
class Solution:
    def sortedSquares(self,arr):
        n=len(arr)

        for i in range(n):
            arr[i]=arr[i]*arr[i]

        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        return arr
Optimal:
class Solution:
    def sortedSquares(self,arr):
        left=0
        right=len(arr)-1
        ans=[0]*len(arr)
        pos=len(arr)-1

        while left<=right:
            if abs(arr[left])>abs(arr[right]):
                ans[pos]=arr[left]*arr[left]
                left+=1
            else:
                ans[pos]=arr[right]*arr[right]
                right-=1

            pos-=1

        return ans
