Brute:
arr = [1, 1, 2, 2, 3, 4, 4]
temp = []
for i in range(len(arr)):
    if arr[i] not in temp:
        temp.append(arr[i])
print(temp)

Optimal:
arr = [1, 1, 2, 2, 3, 4, 4]
j = 0
for i in range(1, len(arr)):
    if arr[i] != arr[j]:
        j = j + 1
        arr[j] = arr[i]
for i in range(j + 1):
    print(arr[i], end=" ")

