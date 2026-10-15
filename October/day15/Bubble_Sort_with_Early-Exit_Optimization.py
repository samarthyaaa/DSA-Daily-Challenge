class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0: # Move left if number is even
                left += 1
            elif nums[right] % 2 != 0: # Move right if number is odd
                right -= 1
            else:
                temp = nums[left]  # Swap the numbers
                nums[left] = nums[right]
                nums[right] = temp

        return nums
