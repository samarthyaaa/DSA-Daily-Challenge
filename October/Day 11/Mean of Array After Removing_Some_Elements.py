class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n=len(arr)
        remove=n//20
        total=0
        for i in range(remove,n-remove):
            total+=arr[i]
        count=n-2*remove
        return float(total)/count
time complexity: O(n log n)
