class Solution(object):
    def commonCharacters(self, s1, s2):
        freq = {}
        result = ""

        for i in range(len(s1)):
            freq[s1[i]] = 1

        for i in range(len(s2)):
            if s2[i] in freq:
                if freq[s2[i]] == 1:
                    result += s2[i]
                    freq[s2[i]] = 0

        return result
