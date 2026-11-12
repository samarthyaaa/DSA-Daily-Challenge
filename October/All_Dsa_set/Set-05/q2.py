Brute:
class Solution:
    def fastest(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr[:3]
Optimal:
class Solution:
    def fastest(self,arr):
        first=float('inf')
        second=float('inf')
        third=float('inf')
        for i in arr:
            if i<first:
                third=second
                second=first
                first=i
            elif i<second:
                third=second
                second=i
            elif i<third:
                third=i
        return [first,second,third]
