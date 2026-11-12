Brute:
arr = [2, 4, 6, 8, 10]
k = 2
threshold = 5
count = 0
for i in range(len(arr) - k + 1):
    total = 0
    for j in range(i, i + k):
        total = total + arr[j]
    avg = total / k
    if avg >= threshold:
        count = count + 1
print(count)
Optimal:
arr = [2, 4, 6, 8, 10]
k = 2
threshold = 5

total = 0
count = 0

for i in range(k):
    total = total + arr[i]
if total >= k * threshold:
    count = count + 1
for i in range(k, len(arr)):
    total = total - arr[i-k]
    total = total + arr[i]
    if total >= k * threshold:
        count = count + 1
print(count)
