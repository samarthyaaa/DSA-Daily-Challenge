Brute force:
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
Optimal solution:
def binary_search(arr, target):
    lo=0, hi=len(arr) - 1
    while lo <= hi:                     
        mid = lo + (hi - lo) // 2       # divides the array in two halfs
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1                
        else:
            hi = mid - 1               
    return lo # returns lo value to show where to put the new element if location didn't found
