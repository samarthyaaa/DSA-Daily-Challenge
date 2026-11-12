brute:
class Solution:
    def sortArray(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
Optimal:
class Solution:
    def sortArray(self,arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
        return arr
