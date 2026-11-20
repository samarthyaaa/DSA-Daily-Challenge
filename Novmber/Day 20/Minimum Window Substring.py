class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("inf")
        ans = ""
        need = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                ch = s[j]

                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
                flag = True
                for ch in need:
                    if ch not in freq or freq[ch] < need[ch]:
                        flag = False
                        break
                if flag:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        ans = s[i:j+1]
        return ans
time complexity:O(n^2)
