word = "abcdefd"
ch = "d"

index = -1

for i in range(len(word)):
    if word[i] == ch:
        index = i
        break

if index != -1:
    ans = ""

    for i in range(index, -1, -1):
        ans += word[i]

    for i in range(index + 1, len(word)):
        ans += word[i]

    print(ans)

else:
    print(word)
