class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        for i in range(n):
            if i==0:
                if n==1 or nums[i]> nums[i+1]:
                    return i
            elif i==n-1:
                if nums[i]>nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                    return i
Time Complexity: O(n)

class Solution:
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
time complexity : O(log n)
