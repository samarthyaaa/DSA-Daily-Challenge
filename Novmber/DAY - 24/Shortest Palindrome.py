def shortestPalin(s):
    n = len(s)
    for i in range(n, 0, -1):
        sub = s[:i]
        if sub == sub[::-1]:
            remaining = s[i:]
            return remaining[::-1] + s
    return s

s = "abcd"
print(shortestPalin(s))
