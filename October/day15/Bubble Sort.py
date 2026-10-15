class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1-i): # swap if left is bigger
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp

     
