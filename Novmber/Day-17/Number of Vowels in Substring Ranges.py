brute force:
s = "abciiide"
queries = [[0, 2], [1, 5], [2, 7]]
for l, r in queries:
    count = 0
    for i in range(l, r + 1):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            count = count + 1
    print(count)
Optimal:
s = "abciiide"
queries = [[0, 2], [1, 5], [2, 7]]
prefix = [0] * (len(s) + 1)
# Build prefix count
for i in range(len(s)):
    prefix[i + 1] = prefix[i]
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        prefix[i + 1] += 1
# Answer each query
for l, r in queries:
    ans = prefix[r + 1] - prefix[l]
    print(ans)

