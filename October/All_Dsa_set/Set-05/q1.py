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
        n=len(arr)
        for i in range(n):
            maxi=i
            for j in range(i+1,n):
                if arr[j]>arr[maxi]:
                    maxi=j
            arr[i],arr[maxi]=arr[maxi],arr[i]
        return arr
