class Solution:
    def countSort(self,s):
        letters="abcdefghijklmnopqrstuvwxyz"
        count=[]*26
        for ch in s: # count how many times letter comes
            for i in range(26):
                if ch==letters[i]:
                    count[i]+=1
                    break
      # makes the sorted string       
        result="" 
        for i in range(26):
            while count[i]>0:
                result +=letters[i]
                count[i]-=1
        return result
