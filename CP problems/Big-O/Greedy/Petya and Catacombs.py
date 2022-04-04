from sys import stdin

n = int(input())
t = [int(x) for x in stdin.readline().split()]
ans = 1
dp = [0] * (n+1)
for i in t:
    ans += dp[i]
    dp[i] = 1

print(ans)
