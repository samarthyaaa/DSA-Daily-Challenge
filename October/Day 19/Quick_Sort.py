class Solution:
    def quickSort(self, arr,low,high):
        if low<high:
            pivot=arr[high]
            i=low
            for j in range(low,high):
                if arr[j]<pivot:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
                    i=i+1
            temp=arr[i]
            arr[i]=arr[high]
            arr[high]=temp
            self.quicksort(arr,low,i-1)
            self.quicksort(arr,i+1,high)
    return arr
