class Solution:
    def freqSort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = ""
        for i in range(len(s)):
            m = 0
            c = ""
            for j in d:
                if d[j] > m:
                    m = d[j]
                    c = j
            if c != "":
                ans += c * m
                d[c] = 0

        return ans
