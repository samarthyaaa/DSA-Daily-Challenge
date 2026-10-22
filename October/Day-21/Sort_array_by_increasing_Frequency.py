class Solution:
    def frequencySort(self, nums):
        freq = {}
        # Count frequency of each number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # Sort using selection sort
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if freq[nums[i]] > freq[nums[j]]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                elif freq[nums[i]] == freq[nums[j]]:
                    if nums[i] < nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
        return nums
