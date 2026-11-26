class Solution:
    def countLetters(self, s):
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                same = True
                for k in range(i, j):
                    if s[k] != s[i]:
                        same = False
                        break
                if same:
                    count += 1

        return count
Optimal:
class Solution:
    def countLetters(self, s):
        count = 0
        length = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                length += 1
            else:
                length = 1
            count = count + length
        if len(s) > 0:
            count = count + 1
        return count
