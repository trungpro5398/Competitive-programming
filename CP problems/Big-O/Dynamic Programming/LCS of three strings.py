from sys import stdin

t = int(input())

while t:
    t -= 1
    n,m,k = [int(x) for x in stdin.readline().split()]
    s, s1, s2 = input().split()
    dp = [[[0 for i in range(k+1)] for i in range(m+1)] for j in range(n+1)]
 
    for i in range(n+1):
        for j in range(m+1):
            for e in range(k+1):
                if i == 0 or j == 0 or e == 0:
                    dp[i][j][e] = 0
                elif s[i-1] == s1[j-1] == s2[e-1]:
                    dp[i][j][e] = dp[i-1][j-1][e-1] + 1
                else:
                    dp[i][j][e] = max( dp[i-1][j][e], dp[i][j-1][e], dp[i][j][e-1], dp[i][j][e])

    print(dp[-1][-1][-1])