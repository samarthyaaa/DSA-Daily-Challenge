Brute:
class Solution:
    def shipWithinDays(self,weights,days):
        low=max(weights)
        high=sum(weights)

        for capacity in range(low,high+1):
            total=0
            count=1

            for i in weights:
                if total+i>capacity:
                    count+=1
                    total=i
                else:
                    total+=i

            if count<=days:
                return capacity
Optimal:
class Solution:
    def shipWithinDays(self,weights,days):
        low=max(weights)
        high=sum(weights)

        while low<high:
            mid=(low+high)//2

            total=0
            count=1

            for i in weights:
                if total+i>mid:
                    count+=1
                    total=i
                else:
                    total+=i

            if count<=days:
                high=mid
            else:
                low=mid+1

        return low
