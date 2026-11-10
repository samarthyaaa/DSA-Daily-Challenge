s = "the sky is blue"
words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
if word != "":
    words.append(word)
ans = ""
for i in range(len(words)-1, -1, -1):
    ans += words[i] + " "

print(ans.strip())
