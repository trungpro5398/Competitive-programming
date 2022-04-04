from sys import stdin

t1 = int(input())

while t1:
    t1 -= 1
    n, w = [int(x) for x in stdin.readline().split()]
    c = [0] * (n+1)
    p = [0] *  (n+1)
    t = [0] *  (n+1)
    for i in range(1,n+1):
        c[i], p[i], t[i] =  [int(x) for x in stdin.readline().split()]
    dp = [[0] * (w+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1,w+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if j >= t[i]:
                dp[i][j] = max(dp[i][j] , p[i]*c[i] + dp[i-1][j-t[i]])

    print(dp[n][w])