
n, m, k =  list(map(int,input().split()))
a =  list(map(int,input().split()))
b =  list(map(int,input().split()))
a1 = [0] * (n+1)
b1 = [0] * (m+1)
a1[1:] = a
b1[1:] = b
dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(2,n+1):
    for j in range(2,m+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif a1[i - 1] == b1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1] + k)