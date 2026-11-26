class Solution:
    def maxPower(self, s):
        maximum = 0
        for i in range(len(s)):
            count = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    count += 1
                else:
                    break
            if count > maximum:
                maximum = count

        return maximum
Time Complexity: O(n**2)
class Solution:
    def maxPower(self, s):
        maximum = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count > maximum:
                maximum = count

        return maximum
Time Complexity: O(n)
