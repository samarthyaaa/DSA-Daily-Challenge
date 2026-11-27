s = "tree"
freq = {}
chars = []
n = len(s)
for i in range(n):
    ch = s[i]
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
        chars = chars + [ch]
for i in range(len(chars)):
    for j in range(len(chars)-1-i):
        if freq[chars[j]] < freq[chars[j+1]]:
            temp = chars[j]
            chars[j] = chars[j+1]
            chars[j+1] = temp
ans = ""# to build answer 
for i in range(len(chars)):
    ch = chars[i]
    for j in range(freq[ch]):
        ans = ans + ch
print(ans)
Optimal: 
s = "tree"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
ans = ""
while len(ans) < len(s):
    max_freq = 0
    max_char = ""
    for ch in freq:
        if freq[ch] > max_freq:
            max_freq = freq[ch]
            max_char = ch
    if max_char == "":
        break
    ans = ans + max_char * max_freq
    freq[max_char] = 0
print(ans)
