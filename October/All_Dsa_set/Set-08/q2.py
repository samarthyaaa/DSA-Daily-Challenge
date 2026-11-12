Brute:
class Solution:
    def searchMatrix(self,matrix,target):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==target:
                    return True
        return False
Optimal:
class Solution:
    def searchMatrix(self,matrix,target):
        if not matrix or not matrix[0]:
            return False

        rows=len(matrix)
        cols=len(matrix[0])

        low=0
        high=rows*cols-1

        while low<=high:
            mid=(low+high)//2
            r=mid//cols
            c=mid%cols

            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                low=mid+1
            else:
                high=mid-1

        return False
