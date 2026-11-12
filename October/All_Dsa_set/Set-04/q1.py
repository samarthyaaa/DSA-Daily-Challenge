arr = [2, 1, 5, 1, 3, 2]
k = 3

total = 0
for i in range(k):
    total = total + arr[i]
maximum = total
for i in range(k, len(arr)):
    total = total - arr[i-k]
    total = total + arr[i]
    if total > maximum:
        maximum = total
print(maximum)
