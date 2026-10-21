def quick_sort(arr, low, high):
    if low < high:
        pivot =arr[high]
        i=low
        j=low
        k=high
        while j<=k
            if arr[j] <= pivot:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i=i+1
                j=j+1
            elif arr[j]>pivot:
                    temp=arr[j]
                    arr[j]=arr[k]
                    arr[k]=temp
                    k=k-1
            else:
                 j=J+1
       self.quicksort(arr,low,i-1)
       self.quicksort(arr,i+1,high)
   return arr
