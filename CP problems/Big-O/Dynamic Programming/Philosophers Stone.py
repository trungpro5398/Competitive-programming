from sys import stdin

t = int(input())

while t:
    t -= 1
    h, w = [int(x) for x in stdin.readline().split()]

    mat = [[0 for i in range(w)] for j in range(h)]

    for i in range(h):
        a = [int(x) for x in stdin.readline().split()]
        for j in range(w):
            mat[i][j] = a[j]
    dp = [[0 for i in range(w)] for j in range(h)]

    for i in range(h):
        for j in range(w):
            dp[i][j] = max(dp[i][j], mat[i][j])
            if i < h-1:
                if j > 0:
                    dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j]+ mat[i+1][j-1])
                if j < w-1:
                    dp[i+1][j + 1] = max( dp[i+1][j + 1],dp[i][j] + mat[i+1][j + 1])

                dp[i + 1][j] = max(dp[i + 1][j] ,dp[i][j] + mat[i + 1][j])

    print(max(dp[-1]))