class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        for i in range(len(s) - len(p) + 1):
            sub = s[i:i + len(p)]

            count1 = {}
            count2 = {}
            for ch in sub:  # Count characters in substring
                if ch not in count1:
                    count1[ch] = 0
                count1[ch] += 1
            for ch in p:    # Count characters in p
                if ch not in count2:
                    count2[ch] = 0
                count2[ch] += 1

            if count1 == count2:      # Compare frequencies
                ans.append(i)

        return ans
