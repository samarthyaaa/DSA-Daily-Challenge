Brute:
arr = [1, 1, 0, 1, 1, 1, 0, 1]
maximum = 0
for i in range(len(arr)):
    count = 0
    if arr[i] == 1:
        for j in range(i, len(arr)):
            if arr[j] == 1:
                count = count + 1
            else:
                break
    if count > maximum:
        maximum = count
print(maximum)
Optimal:
arr = [1, 1, 0, 1, 1, 1, 0, 1]
count = 0
maximum = 0

for i in range(len(arr)):
    if arr[i] == 1:
        count = count + 1
    else:
        count = 0
    if count > maximum:
        maximum = count

print(maximum)

