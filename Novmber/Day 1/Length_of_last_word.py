class Solution(object):
    def lengthOfLastWord(self, s):
        i=0
        char_count=0
        word_count=0
        while i<len(s):
            if s[i]!=" ":
                if word_count==0:
                   char_count=0
                word_count=1
                char_count+=1
            else:
                word_count=0
            i+=1
        return char_count
Time complexity: O(n)
Space Complexity: O(1)
