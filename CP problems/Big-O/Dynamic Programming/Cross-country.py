from sys import stdin

t = int(input())

while t:
    a = [int(x) for x in stdin.readline().split()]

    ans = 0
    while True:
        b = [int(x) for x in stdin.readline().split()]
        dp = [[0 for i in range(len(b))] for j in range(len(a))]
        if len(b) == 1:
            break

        for i in range(len(a)):
            for j in range(len(b)):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]  + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        ans = max(dp[-1][-1], ans)
    print(ans)
    t -= 1
