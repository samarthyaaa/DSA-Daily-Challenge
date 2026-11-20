class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                chars = set(sub)
                nice = True
                for ch in chars:
                    if ch.lower() not in chars or ch.upper() not in chars:
                        nice = False
                        break
                if nice and len(sub) > len(longest):
                    longest = sub
        return longest
