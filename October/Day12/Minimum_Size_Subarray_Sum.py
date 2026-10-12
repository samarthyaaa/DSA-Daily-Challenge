def findMinLength(target, nums):
    left = 0
    total = 0
    ans = len(nums) + 1

    for right in range(len(nums)):
        total += nums[right]  # Add the next number

        while total >= target:
            length = right - left + 1

            if length < ans:
                ans = length  # Save the smaller length

            total -= nums[left]  # Remove the first number
            left += 1  # Move left forward

    if ans == len(nums) + 1:
        return 0  # No valid subarray found

    return ans
