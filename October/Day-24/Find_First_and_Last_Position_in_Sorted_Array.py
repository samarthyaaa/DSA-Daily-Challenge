Brute force:
class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
Optimal solution:       
def searchRange(nums, target):
    def findFirst():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    def findLast():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    return [findFirst(), findLast()]
