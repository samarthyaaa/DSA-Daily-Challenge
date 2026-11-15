class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1, n // 2 + 1):  #  it Checks all substring lengths
            # Length must divide the string 
            if n % i == 0:
                sub = s[:i]
                if sub * (n // i) == s:
                    return True

        return False
