from sys import stdin

t = int(input())

while t:
    t -= 1
    k = int(input())
    n = int(input())
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    b = [int(x) for x in stdin.readline().split()]
    a = [0] * (n+1)
    for i in range(0, n):
        a[i+1] = b[i]
    for i in range(1,k+1):
        sav = -10**9
        for j in range(2,n+1):
            sav = max(sav, dp[i-1][j-1] - a[j-1])
            dp[i][j] = max(dp[i][j-1], a[j] + sav)
    print(dp[k][n])