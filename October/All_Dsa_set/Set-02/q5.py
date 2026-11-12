Brute:
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
k = k % n
for i in range(k):
    last = arr[n - 1]
    for j in range(n - 1, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = last
print(arr)
optimal:

arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n
# Reverse entire array
left = 0
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left = left + 1
    right = right - 1
# Reverse first k elements
left = 0
right = k - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left = left + 1
    right = right - 1
# Reverse remaining elements
left = k
right = n - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left = left + 1
    right = right - 1

print(arr)

