class Solution:
    def merge(self,intervals):
        n=len(intervals)

        for i in range(n):
            for j in range(n-1-i):
                if intervals[j][0]>intervals[j+1][0]:
                    intervals[j],intervals[j+1]=intervals[j+1],intervals[j]

        ans=[]

        for i in intervals:
            if not ans or i[0]>ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1]=max(ans[-1][1],i[1])

        return ans
