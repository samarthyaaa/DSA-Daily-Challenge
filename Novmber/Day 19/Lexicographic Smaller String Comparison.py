class Solution:
    def findLongestWord(self, s, dictionary):
        ans = ""
        for word in dictionary:
            i = 0
            j = 0
            while i < len(s):
                if s[i] == word[j]:
                    j += 1

                    if j == len(word):
                        break
                i += 1
            if j == len(word):
                if len(word) > len(ans):
                    ans = word

                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans
