class Solution(object):
    def LongSubstr(self, s):
        maxlen = 0
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub = sub + s[j]
                if len(sub) > maxlen:
                    maxlen = len(sub)
        return maxlen


class Solution(object):
    def LongSubstr(self, s):
        seen = {}
        left = 0
        maxlen = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            length = right - left + 1
            if length > maxlen:
                maxlen = length
        return maxlen


