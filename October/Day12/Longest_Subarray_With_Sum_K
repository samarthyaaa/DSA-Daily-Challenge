class Solution:
    def longestSubarray(self, arr, k):
        start = 0
        t = 0
        longest = 0

        for end in range(len(arr)):
            # Add the current element
            t += arr[end]
        
            while t > k and start <= end:  # Remove elements if the sum is greater than k
                t -= arr[start]
                start += 1

            if t == k:   # Check if the sum equals k
                size = end - start + 1

               
                if size > longest:  # Update the longest length
                    longest = size

        return longest
