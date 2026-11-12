brute:
class Solution:
    def intersection(self,a,b):
        ans=[]

        for i in a:
            for j in b:
                if i==j:
                    if i not in ans:
                        ans.append(i)
                    break

        return ans
