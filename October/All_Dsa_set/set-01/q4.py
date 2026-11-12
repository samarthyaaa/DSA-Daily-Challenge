Brute Force: 
arr = [1, 7, 3, 6, 5, 6]

for i in range(len(arr)):
    left = 0
    right = 0
    for j in range(i):
        left = left + arr[j]
    for j in range(i + 1, len(arr)):
        right = right + arr[j]
    if left == right:
        print(i)
        break
else:
    print(-1)
Optimal:

arr = [1, 7, 3, 6, 5, 6]

total = 0
for i in range(len(arr)):
    total = total + arr[i]
left = 0
for i in range(len(arr)):
    right = total - left - arr[i]
    if left == right:
        print(i)
        break
    left = left + arr[i]
else:
    print(-1)
