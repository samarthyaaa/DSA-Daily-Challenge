class Solution(object):
    def longestPalindrome(self, s):
        freq = {}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        length = 0
        odd_found = False

        for ch in freq:
            if freq[ch] % 2 == 0:
                length += freq[ch]
            else:
                length += freq[ch] - 1
                odd_found = True

        if odd_found:
            length += 1

        return length
