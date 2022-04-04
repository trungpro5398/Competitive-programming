from sys import stdin


dp = []
dp.append(1)
for i in range(2, 1008):
    mark = 0
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            mark = 1
            break
    if not mark:
        dp.append(i)

while True:
    a = [int(x) for x in stdin.readline().split()]
    if len(a) == 0:
        break

    n, c = a[0], a[1]
    print("{} {}: ".format(n, c), end="")
    l = 0
    lst = []
    for i in range(0, 1010):
        if dp[i] <= n:
           lst.append(dp[i])
           l += 1
        else:
            break
    if l & 1:
        c = c * 2 - 1
    else:
        c *= 2
    if c > l:
        c = l
    l1 = l // 2 - c// 2

    for i in range(0, c):
        print(lst[l1], end= " ")
        l1 += 1
    print()
