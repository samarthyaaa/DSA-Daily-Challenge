class Solution:
    def minSubArrayLen(self, target, nums):
        start = 0
        summ = 0
        smallest = len(nums) + 1

        for end in range(len(nums)):
            summ += nums[end]  # Add the next number

            while summ >= target:
                length = end - start + 1

                if length < smallest:
                    smallest = length  # Save the smaller length

                summ -= nums[start]  # Remove the first number
                start += 1  # Move start forward

        if smallest == len(nums) + 1:
            return 0  # No valid subarray found

        return smallest
