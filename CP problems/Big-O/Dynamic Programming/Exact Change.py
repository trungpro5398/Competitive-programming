import math

t = int(input())

while t:
    t -= 1
    price = int(input())
    n = int(input())
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    dp = [[math.inf] * (price + 10010) for _ in range(n + 2)]
    dp[0][0] = 0
    dp[0][arr[0]] = 1
    for i in range(1, n):
        for j in range(0, price + 10010):
            if j >= arr[i]:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i - 1][j - arr[i]])
            else:
                dp[i][j] = dp[i-1][j]

    for i in range(price, price+10010):
        if dp[n-1][i] < math.inf:
            print("{} {}".format(i, dp[n-1][i]))
            break