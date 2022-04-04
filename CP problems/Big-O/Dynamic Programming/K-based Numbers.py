
n = int(input())
k = int(input())
dp = [0] * 19
cnt_0 = [0] * 19
cnt_k = [0] * 19
dp[1] = k - 1
cnt_0[1] = 0
cnt_k[1] = k - 1
for i in range(2, n+1):
    if i == 2:
        cnt_0[i] = dp[i-1]
    else:
        cnt_0[i] = cnt_k[i-1]
    cnt_k[i] = cnt_k[i-1] * (k-1) + cnt_0[i-1] * (k-1)
    dp[i] =  cnt_k[i] +  cnt_0[i]

print(max(dp))