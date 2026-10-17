class Solution:
    def sortArray(self, nums):
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > temp: # Shift bigger elements to  right side
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp  # Place elements in the correct position
        return nums
