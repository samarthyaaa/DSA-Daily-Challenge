Brute:
arr = [10, 20, 4, 45, 99]
for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[j] > arr[i]:
            count = count + 1
    if count == 1:
        print(arr[i])
        break
else:
    print(-1)
Optimal:

arr = [10, 20, 4, 45, 99]
first = float('-inf')
second = float('-inf')

for i in range(len(arr)):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second and arr[i] != first:
        second = arr[i]
if second == float('-inf'):
    print(-1)
else:
    print(second)
