Brute force:
class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True
        return False
# time complexity : O(m*n))
Optimal Solution:
class Solution(object):
    def searchMatrix(self, matrix, target):
        low,high=0,len(matrix)*len(matrix[0])-1
        while low <= high:
            mid =low+(high-low)//2
            row=mid //len(matrix[0])
            column=mid %len(matrix[0])
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                low=mid+1
            else:
                high=mid-1
        return False
# time complexity : O(log(m * n))
