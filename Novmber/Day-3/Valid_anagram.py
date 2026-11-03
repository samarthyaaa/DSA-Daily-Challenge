brute force :
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count1 = 0
            count2 = 0

            for j in range(len(s)):
                if s[i] == s[j]:
                    count1 += 1

                if s[i] == t[j]:
                    count2 += 1

            if count1 != count2:
                return False

        return True
