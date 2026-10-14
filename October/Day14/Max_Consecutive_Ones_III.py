class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        zero = 0
        answer = 0
        while right < len(nums):
            if nums[right] == 0:
                zero += 1 # Count zeros
            while zero > k:
                if nums[left] == 0:
                    zero -= 1 # Remove a zero
                left += 1 # Move left pointer

            length = right - left + 1
            if length > answer:
                answer = length# Update maximum

            right += 1 # Move right pointer

        return answer
