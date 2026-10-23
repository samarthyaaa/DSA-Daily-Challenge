class Solution:
    def insertionsort(self,arr):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=arr[j]
    return arr
        
