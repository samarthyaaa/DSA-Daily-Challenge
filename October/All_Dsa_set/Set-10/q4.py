Brute:
class Solution:
    def threeSum(self,arr):
        ans=[]
        n=len(arr)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        triplet=sorted([arr[i],arr[j],arr[k]])

                        if triplet not in ans:
                            ans.append(triplet)

        return ans
Optimal:
class Solution:
    def threeSum(self,arr):
        arr=sorted(arr)
        ans=[]
        n=len(arr)

        for i in range(n-2):
            if i>0 and arr[i]==arr[i-1]:
                continue

            left=i+1
            right=n-1

            while left<right:
                total=arr[i]+arr[left]+arr[right]

                if total==0:
                    ans.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1

                    while left<right and arr[left]==arr[left-1]:
                        left+=1

                    while left<right and arr[right]==arr[right+1]:
                        right-=1

                elif total<0:
                    left+=1
                else:
                    right-=1

        return ans
