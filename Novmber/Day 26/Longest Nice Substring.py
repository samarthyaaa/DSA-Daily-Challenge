class Solution:
    def longstring(self, s):
        ans = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                nice = True
                for ch in sub:
                    if ord(ch) >= 97 and ord(ch) <= 122:
                        if chr(ord(ch)-32) not in sub:
                            nice = False
                            break
                    elif ord(ch) >= 65 and ord(ch) <= 90:
                        if chr(ord(ch)+32) not in sub:
                            nice = False
                            break
                if nice and len(sub) > len(ans):
                    ans = sub
        return ans

optimal:
class Solution:
    def longeststring(self, s):
        if len(s) < 2:
            return ""
        for i in range(len(s)):
            ch = s[i]
            if ord(ch) >= 97 and ord(ch) <= 122:
                opposite = chr(ord(ch) - 32)
            else:
                opposite = chr(ord(ch) + 32)
            if opposite not in s:
                left = self.longeststring(s[:i])
                right = self.longeststring(s[i+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s
