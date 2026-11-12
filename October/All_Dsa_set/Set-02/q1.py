Brute:
arr = [1, 2, 1, 3, 2, 1, 1]
max_count = 0
winner = -1
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1
    if count > max_count:
        max_count = count
        winner = arr[i]

print(winner)
Optimal:
arr = [1, 2, 1, 3, 2, 1, 1]
freq = {}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] = freq[arr[i]] + 1
    else:
        freq[arr[i]] = 1
winner = -1
maximum = 0
for i in freq:
    if freq[i] > maximum:
        maximum = freq[i]
        winner = i
print(winner)

