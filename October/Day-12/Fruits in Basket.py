class Solution:
    def totalFruit(self, fruits):
        left=0
        count={}
        maxlen=0
        for right in range(len(fruits)):
            fruit=fruits[right]
            if fruit in count:
                count[fruit]+=1
            else: 
                count[fruit]=1
            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            length=right-left+1
            maxlen=max(maxlen,length)
        return maxlen
