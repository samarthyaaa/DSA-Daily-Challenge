def rearrange(s,target):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    count=0
    while True:
        flag=1
        for ch in target:
            if ch not in freq or freq[ch]==0:
                flag=0
                break
        if flag==0:
            break
        for ch in target:
            freq[ch]-=1
        count+=1
    return count
s="ilovecoding"
target="code"

print(rearrange(s,target))
Time Complexity: (O(n+k*m))
