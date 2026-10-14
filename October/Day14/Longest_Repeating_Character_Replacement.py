class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        ans = 0
        freq = {}
        maxf = 0
        for right in range(len(s)):
            ch = s[right]

            if ch in freq:   # Count the current letter
                freq[ch] += 1
            else:
                freq[ch] = 1

            if freq[ch] > maxf: # Update highest frequency
                maxf = freq[ch]

            while right - left + 1 - maxf > k:# It Shrink window if replacements exceed k
                freq[s[left]] -= 1
                left += 1

            length = right - left + 1 #It Updates longest valid length
            if length > ans:
                ans = length
        return ans
