import math
from sys import stdin


def C():
    n = int(stdin.readline())
    res = 1
    res1 = 1
    cols = 2
    rows = n
    arr = [[0 for i in range(cols)] for j in range(rows)]
    dp = [[0 for i in range(cols*2)] for j in range(rows)]
    for i in range(n):
        c = [int(x) for x in stdin.readline().split()]
        a, b = c[0], c[1]
        arr[i][0], arr[i][1] = a, b

    dp[0][0], dp[0][1], dp[0][2], dp[0][3] = arr[0][0], arr[0][0], arr[0][1], arr[0][1]
    for i in range(1,n):
        dp[i][0] = math.gcd(dp[i - 1][0], arr[i][0])
        dp[i][1] = math.gcd(dp[i - 1][2], arr[i][0])
        dp[i][2] = math.gcd(dp[i - 1][1], arr[i][1])
        dp[i][3] = math.gcd(dp[i - 1][3], arr[i][1])

    res3 = 0
    for i in range(0, cols):

        res1 = dp[n-1][i]

        for j in range(cols, cols*2):
            res2 = dp[n - 1][j]
            res3 = max((res3, int(res1 * res2 / math.gcd(res1, res2))))

    print(res3)
C()