class Solution:
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        a = [0] * 26 #Count s1 letters
        b = [0] * 26 #Count s2 window

        for i in range(n1):
            a[ord(s1[i]) - 97] += 1
            b[ord(s2[i]) - 97] += 1
        if a == b:
            return True
        for i in range(n1, n2):
            b[ord(s2[i]) - 97] += 1 #Add new letter
            b[ord(s2[i - n1]) - 97] -= 1 #Remove old letter

            if a == b:
                return True
        return False
