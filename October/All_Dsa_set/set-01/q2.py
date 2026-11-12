Brute Force:
arr = [5, 1, 3, 4, 3, 5]

for i in range(len(arr)):
    for j in range(i):
        if arr[i] == arr[j]:
            print(arr[i])
            exit()
print(-1)

Optimal:
arr = [5, 1, 3, 4, 3, 5]

seen = set()
for i in range(len(arr)):
    if arr[i] in seen:
        print(arr[i])
        break
    seen.add(arr[i])
else:
    print(-1)

