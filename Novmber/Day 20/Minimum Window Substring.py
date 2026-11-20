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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        window = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        left = 0
        right = 0
        formed = 0
        required = len(need)
        min_len = float("inf")
        start = 0
        while right < len(s):

            ch = s[right]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            # Window is valid
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                # Remove character from left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1
            right += 1
        if min_len == float("inf"):
            return ""
        return s[start:start + min_len]
