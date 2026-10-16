class Solution(object):
    def frequencySort(self, s):
        d={}
        for ch in s: # count each character
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        chars = list(d)
        for i in range(len(chars)): # sort by frequency
            for j in range(i+1,len(chars)):
                if d[chars[j]]>d[chars[i]]:
                    chars[i], chars[j]=chars[j],chars[i]
        ans=""
        for ch in chars: # repeat characters by count
            ans+=ch*d[ch]
        return ans
