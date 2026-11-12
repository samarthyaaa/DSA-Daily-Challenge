Brute:
arr = [101, 102, 103, 102, 104]
seen = set()

for i in range(len(arr)):
    if arr[i] in seen:
        print(arr[i])
        break
    seen.add(arr[i])

else:
    print(-1)
