text = input("Enter text: ")
pat = input("Enter pattern: ")

n = len(text)
m = len(pat)
found = False

for i in range(n - m + 1):
    j = 0
    while j < m and text[i+j] == pat[j]:
        j = j + 1
    if j == m:
        print(i)
        found = True
        break
if found == False:
    print(-1)
