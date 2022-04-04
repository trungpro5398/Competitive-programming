from sys import stdin



t = int(stdin.readline())

while t:
    t -= 1
    n = int(input())
    a = [int(x) for x in stdin.readline().split()]
    if n %2 == 0:
        print(0)
        continue
    dp = [0] * n
    dp[0] = dp[n-1] = n
    cnt = n + (n-2)
    for i in range(1, n // 2):
        dp[i] = cnt
        cnt += 1
    if n % 2 == 0:
        cnt -= 1
    for i in range(n//2, n-1):
        dp[i] = cnt
        cnt -= 1
    res = 0

    for i in range(len(dp)):
        if dp[i] % 2 == 1 :
            res ^= a[i]
    print(res)