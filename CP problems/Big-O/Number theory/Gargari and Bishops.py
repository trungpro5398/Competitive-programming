from sys import stdin

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    k = [int(x) for x in stdin.readline().split()]
    for j in range(n):
        a[i][j] = k[j]
dp = [0] * 5020
dp1 = [0] * 5020
for i in range(n):
    for j in range(n):
        k = i - j + n
        k1 = i + j
        dp[k] += a[i][j]
        dp1[k1] += a[i][j]
val = [-10**18] * 2
res = [[0 for _ in range(2)] for i in range(2)]
for i in range(n):
    for j in range(n):
        k = i - j + n
        k1 = i + j
        x = (i+j) % 2
        sum = (dp[k] + dp1[k1] - a[i][j])
        val[x] = max(val[x], sum)
        if sum == val[x]:
            res[x][0] = i + 1
            res[x][1] = j + 1
print(val[0] + val[1])
print("{} {} {} {}".format(res[0][0], res[0][1], res[1][0], res[1][1]))