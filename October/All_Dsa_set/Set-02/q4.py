Brute:
arr = [10, 20, 30, 40, 50]
queries = [[0, 2], [1, 3]]
for i in range(len(queries)):
    left = queries[i][0]
    right = queries[i][1]
    total = 0
    for j in range(left, right + 1):
        total = total + arr[j]
    print(total)
Optimal:
arr = [10, 20, 30, 40, 50]
queries = [[0, 2], [1, 3]]
prefix = []
total = 0
for i in range(len(arr)):
    total = total + arr[i]
    prefix.append(total)
for i in range(len(queries)):
    left = queries[i][0]
    right = queries[i][1]
    if left == 0:
        ans = prefix[right]
    else:
        ans = prefix[right] - prefix[left - 1]

    print(ans)
