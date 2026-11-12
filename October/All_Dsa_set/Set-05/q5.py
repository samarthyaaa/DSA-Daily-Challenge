Brute:
class Solution:
    def findKthLargest(self,arr,k):
        n=len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr[k-1]
