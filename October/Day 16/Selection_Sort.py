class Solution: 
    def selectionSort(self, arr):
        for i in range (len(arr)):
            temp=i
            for j in range (i+1,len(arr)):
                if arr[temp]>arr[j]:
                    temp=j #stores smallest element
            arr[i],arr[temp]=arr[temp],arr[i] # swap the elements
        return arr
    
