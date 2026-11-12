class Solution:
    def popularity(self,arr):
        count={}
        unique=[]

        for i in arr:
            if i not in count:
                count[i]=0
                unique.append(i)
            count[i]+=1
        bucket=[[] for i in range(len(arr)+1)]

        for i in unique:
            bucket[count[i]].append(i)

        ans=[]
        for i in range(len(arr),0,-1):
            for j in bucket[i]:
                ans.append(j)

        return ans
