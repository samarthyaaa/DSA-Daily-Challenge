class Solution:
    def wiggleSort(self, nums):
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
            else:
                if nums[i] < nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
