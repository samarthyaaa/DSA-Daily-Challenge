Brute:
class Solution:
    def trimmedMean(self,arr):
        n=len(arr)

        for i in range(n):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        k=n//20
        total=0

        for i in range(k,n-k):
            total+=arr[i]

        return total/(n-2*k)
Optimal:
class Solution:
    def trimmedMean(self,arr):
        count=[0]*101

        for i in arr:
            count[i]+=1

        n=len(arr)
        k=n//20
        remove=k
        total=0

        for i in range(101):
            take=min(count[i],remove)
            count[i]-=take
            remove-=take

            if remove==0:
                break

        remove=k

        for i in range(100,-1,-1):
            take=min(count[i],remove)
            count[i]-=take
            remove-=take

            if remove==0:
                break

        for i in range(101):
            total+=i*count[i]

        return total/(n-2*k)
