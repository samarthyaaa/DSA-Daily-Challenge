#brute force 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        for i in range(len(s)):
            seen = ""

            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen += s[j] #Add character
                if len(seen) > ans:
                    ans = len(seen)
        return ans
time complexity O(n**2)



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]
            # Move left if character repeats
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            # Update longest length
            length = right - left + 1
            if length > ans:
                ans = length
        return ans

time complexity O(n)
