arr = [0, 1, 0, 3, 12]

temp = []

for i in range(len(arr)):
    if arr[i] != 0:
        temp.append(arr[i])

for i in range(len(arr)):
    if arr[i] == 0:
        temp.append(0)

print(temp)
