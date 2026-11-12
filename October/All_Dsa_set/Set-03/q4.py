a = [1, 3, 5]
b = [2, 4, 6]
c = []

for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    for j in range(len(c)-1-i):

        if c[j] > c[j+1]:
            temp = c[j]
            c[j] = c[j+1]
            c[j+1] = temp

print(c)
