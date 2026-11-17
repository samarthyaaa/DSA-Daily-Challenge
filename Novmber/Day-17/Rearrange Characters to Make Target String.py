brute force:
s = "ilovecoding"
target = "code"
temp = list(s)
ans = 0
while True:
    used = [False] * len(temp)
    possible = True
    for ch in target:
        found = False
        for i in range(len(temp)):
            if temp[i] == ch and used[i] == False:
                used[i] = True
                found = True
                break

        if found == False:
            possible = False
            break

    if possible == False:
        break

    new_temp = []

    for i in range(len(temp)):
        if used[i] == False:
            new_temp.append(temp[i])

    temp = new_temp
    ans = ans + 1

print(ans)
Optimal:
s = "ilovecoding"
target = "code"

a = [0] * 26
b = [0] * 26
for ch in s:# Count characters in s
    a[ord(ch) - ord('a')] += 1
for ch in target:# Count characters in target
    b[ord(ch) - ord('a')] += 1
ans = len(s)
for i in range(26): # Find minimum possible copies
    if b[i] > 0:
        x = a[i] // b[i]
        if x < ans:
            ans = x
print(ans)


