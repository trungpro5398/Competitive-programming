import math
from sys import stdin

k = int(input())
while k:
    k -= 1
    S = input()
    t, a = [int(x) for x in stdin.readline().split()]
    n = int(input())
    ti, ai, wi = [0] * n, [0] * n, [0] * n
    for i in range(n):
        ti[i],ai[i],wi[i] = [int(x) for x in stdin.readline().split()]
    dp = [[[0 for _ in range(a+10)] for _ in range(t+10)] for _ in range(n+10)]
    for i in range(t+1):
        for j in range(a+1):
            if j <= ai[1] and i <= ti[1]:
                dp[0][i][j] = wi[1]
            else:
                dp[0][i][j] = math.inf

    dp[0][0][0] = 0
    for i in range(1,n):
        for j in range(t+1):
            for k in range(a+1):
                dp[i][j][k] = min(dp[i-1][j][k], wi[i] + dp[i-1][max(0,j-ti[i])][max(k-ai[i],0)])
    print(dp[n-1][t-1][a-1])
