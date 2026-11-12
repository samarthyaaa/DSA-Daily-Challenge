Brute:
s = list("COUPON")
i = 0
j = len(s) - 1
while i < j:
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    i = i + 1
    j = j - 1
for i in range(len(s)):
    print(s[i], end="")
