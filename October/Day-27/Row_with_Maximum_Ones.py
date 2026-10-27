class Solution(object):
    def rowAndMaximumOnes(self, mat):
        max=0
        ans=0
        for i in range(len(mat)):
                count=0
                for j in range(len(mat[0])):
                    if mat[i][j]==1:
                        count+=1

                if count > max:
                    max=count
                    ans=i
        return [ans,max]
