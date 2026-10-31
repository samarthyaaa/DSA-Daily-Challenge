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
optimal:
class Solution:
    def frequencySort(self, nums):
        freq = {}
        # Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # Merge sort
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            ans = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if freq[left[i]] < freq[right[j]]:
                    ans.append(left[i])
                    i += 1
                elif freq[left[i]] > freq[right[j]]:
                    ans.append(right[j])
                elif left[i] > right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            while i < len(left):
                ans.append(left[i])
                i += 1
            while j < len(right):
                ans.append(right[j])
                j += 1
            return ans
        return mergeSort(nums)
