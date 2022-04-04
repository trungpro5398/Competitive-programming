
t =int(input())
while t:
    t -= 1
    n = int(input())

    tr = [0] * n
    for i in range(n):
        tr[i] = int(input())

    lis = [0] * n
    dp = [0] * n
    
    for i in range(n-1,-1,-1):
        lis[i] = 1
        dp[i] = 1
        for j in range(0, n):
            if tr[i] > tr[j]:
                dp[i] = max(dp[j]+1,dp[i] )
            elif tr[i] < tr[j]:
                lis[i] = max(lis[i], lis[j]+1)
    res = 0
    for i in range(0,n):
        res = max(res, dp[i] + lis[i] - 1)
    print(res)
