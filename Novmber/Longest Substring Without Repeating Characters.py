class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub = sub + s[j]
                if len(sub) > max_len:
                    max_len = len(sub)

        return max_len
