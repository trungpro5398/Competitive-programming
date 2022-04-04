

dp = {}
dp[0] = 0
dp[1] = 1

def cal(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = max(n, cal(n//2) + cal(n//3) + cal(n//4))
        return dp[n]
try:
    while True:
        n = int(input())
        print(cal(n))
except:
    pass