Brute:
class Solution:
    def sortReadings(self,arr):
        n=len(arr)

        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        return arr
Optimal:
class Solution:
    def sortReadings(self,arr):
        def quicksort(low,high):
            if low>=high:
                return

            pivot=arr[(low+high)//2]
            i=low
            j=low
            k=high

            while j<=k:
                if arr[j]<pivot:
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j+=1
                elif arr[j]>pivot:
                    arr[j],arr[k]=arr[k],arr[j]
                    k-=1
                else:
                    j+=1

            quicksort(low,i-1)
            quicksort(k+1,high)

        quicksort(0,len(arr)-1)
        return arr
