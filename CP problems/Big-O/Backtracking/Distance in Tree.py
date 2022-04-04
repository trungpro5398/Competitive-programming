from sys import stdin

n, m = [int(x) for x in stdin.readline().split()]
adj = [[] for _ in range(n+1)]
dp = [0] * (n+1)
vis = [0] * (n+1)
for i in range(n-1):
    x, y = [int(x) for x in stdin.readline().split()]
    adj[x].append(y)

def dfs(s, cnt):
    if vis[s] or s > n:
        return cnt
    vis[s] = 1
    dp[s] = cnt
    for i in adj[s]:
        dfs(i, cnt+1)

dfs(1,0)
ans = [0] * (n+1)
for i in range(1, n+1):
    ans[dp[i]] += 1
cnt = 0

for i in range(1, n+1):
    sav = dp[i] + m
    if sav <= n+1:
        cnt += ans[sav]
print(dp, cnt)