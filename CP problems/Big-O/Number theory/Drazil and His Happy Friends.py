from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
b = [0] * 101
g = [0] * 101
k = [int(x) for x in stdin.readline().split()]
for i in range(1, len(k)):
    b[k[i]] = 1
k = [int(x) for x in stdin.readline().split()]
for i in range(1, len((k))):
    g[k[i]] = 1
for i in range(10001):
    b1 = i % n
    g1 = i % m
    if b[b1] or g[g1]:
        b[b1], g[g1] = 1 , 1


res = True
for i in range(n):
    if b[i] == 1:
        continue

    res = False
    break
if res:
    for i in range(m):
        if g[i] == 1:
            continue

        res = False
        break
if res:
    print("Yes")
else:
    print('No')