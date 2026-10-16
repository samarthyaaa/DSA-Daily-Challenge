class Solution: 
    def KSmallest(self, arr,k):
        for i in range (k):
            temp=i 
            for j in range (i+1,len(arr)):
                if arr[temp]>arr[j]:
                    temp=j #stores smallest element's index
            arr[i],arr[temp]=arr[temp],arr[i] # swap the elements
        return arr[:k] # return K smallest elements
    
