class Solution(object):
    def canPermutePalindrome(self, s):
        freq = {}

        for i in range(len(s)):
            if s[i] in freq:r
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        odd_count = 0

        for ch in freq:
            if freq[ch] % 2 != 0:
                odd_count += 1

        if odd_count > 1:
            return False

        return True
