def reorganize(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    n=len(s)
    for ch in freq:
        if freq[ch]>(n+1)/2:
            return ""
    ans=""
    prev=""
    for i in range(n):
        maxch=""
        maxfreq=0
        for ch in freq:
            if ch!=prev and freq[ch]>maxfreq:
                maxfreq=freq[ch]
                maxch=ch
        if maxch=="":
            return ""
        ans+=maxch
        freq[maxch]-=1
        prev=maxch
    return ans


print(reorganize("aab"))
