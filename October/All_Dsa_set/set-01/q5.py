Brute:
arr = [1, 2, 4, 5]
n = 5

for i in range(1, n + 1):
    found = False
    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break
    if found == False:
        print(i)
        break
Optimal:

arr = [1, 2, 4, 5]
n = 5
total = n * (n + 1) // 2
actual = 0
for i in range(len(arr)):
    actual = actual + arr[i]
missing = total - actual
print(missing)
