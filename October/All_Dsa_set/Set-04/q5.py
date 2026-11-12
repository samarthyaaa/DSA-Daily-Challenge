s = input("Enter string: ")
maximum = 0
for i in range(len(s)):
    seen = ""
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen = seen + s[j]
        if len(seen) > maximum:
            maximum = len(seen)

print(maximum)
