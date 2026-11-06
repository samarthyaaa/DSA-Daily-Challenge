Brute force:
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        used=[False] * len(magazine)
        for i in range(len(ransomNote)):
            found=False
            for j in range(len(magazine)):
                if ransomNote[i]==magazine[j] and used[j]==False:
                    used[j]=True
                    found =True
                    break
            if found==False:
                return False
        return True
