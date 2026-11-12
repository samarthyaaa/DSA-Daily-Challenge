Brute:
arr = [4, 5, 1, 2, 1, 4, 5]
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1
    if count == 1:
        print(arr[i])
        break
else:
    print(-1)
Optimal:
arr = [4, 5, 1, 2, 1, 4, 5]
freq = {}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] = freq[arr[i]] + 1
    else:
        freq[arr[i]] = 1
for i in range(len(arr)):
    if freq[arr[i]] == 1:
        print(arr[i])
        break
else:
    print(-1)

