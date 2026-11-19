class Solution:
    def findLongestWord(self, s, dictionary):
        ans = ""
        for word in dictionary:
            i = 0
            j = 0
          
            while i < len(s) and j < len(word): # Check if word is a subsequence of s
                if s[i] == word[j]:
                    j += 1

                i += 1

           
            if j == len(word): # If all characters of word matched

                if len(word) > len(ans):
                    ans = word

                elif len(word) == len(ans) and word < ans:
                    ans = word

        return ans
