class Solution(object):
    def longestCommonPrefix(self, strs):
        i=0
        answer=""
        while i<len(strs[0]):
            j=1
            while j<len(strs):
                if i>=len(strs[j]) or strs[j][i] !=strs[0][i]:
                    return answer
                j+=1
            answer += strs[0][i]
            i += 1
        return answer
