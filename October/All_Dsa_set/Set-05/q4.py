Brute:
class Solution:
    def inversionCount(self,arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    count=count+1
        return count
