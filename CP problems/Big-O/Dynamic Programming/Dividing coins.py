from sys import stdin

t1 = int(input())

while t1:
    t1 -= 1
    m = int(input())
    a = [int(x) for x in stdin.readline().split()]
    coins = [0] * (len(a)+1)
    for  i in range(1,len(a)+1):
        coins[i] = a[i-1]
    res = sum(a)
    dp = [[0] * (res+1) for _ in range(m+1)]
    for i in range(1, m + 1):
        for j in range(res//2 + 1):

            if j >= coins[i]:
                dp[i][j] = max(dp[i-1][j],coins[i] + dp[i - 1][j - coins[i]])
            else:
                dp[i][j] = dp[i-1][j]

    print(res - 2 * dp[m][res//2])