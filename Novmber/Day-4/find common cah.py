class Solution(objects):
    def commonchar(self,s1,s2):
        result=" "
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    if s1 not in result:
                        result+=s1[i]
        return result


    
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
