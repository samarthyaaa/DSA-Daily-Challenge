class Solution:
    def findAnagrams(self, s, p):
        ans = []                 # Store starting indices
        n = len(s)               
        m = len(p)             

        for i in range(n - m + 1): 
            a = [0] * 26         # Count s characters
            b = [0] * 26         # Count p characters

            for j in range(m):
                for k in range(26):
                    if s[i + j] == chr(k + 97):
                        a[k] += 1    # Count window letter
                    if p[j] == chr(k + 97):
                        b[k] += 1    # Count p letter

            if a == b:            # Check if anagram
                ans.append(i)     # Save starting index

        return ans               
