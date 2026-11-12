s = list("hello")
vowels = "aeiou"

i = 0
j = len(s) - 1
while i < j:
    if s[i] not in vowels:
        i = i + 1
    elif s[j] not in vowels:
        j = j - 1
    else:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

        i = i + 1
        j = j - 1

for i in range(len(s)):
    print(s[i], end="")
