from sys import stdin

t = int(input())



while t:
    t -= 1
    n = int(input())
    arr = [[] for j in range(n+1)]
    x = [0] * (n+1)
    y = [0] * (n+1)
    for i in range(n):
        x[i],y[i]  = [int(x) for x in stdin.readline().split()]
        arr[x[i]].append(y[i])


    def dfs(v):
        global vis, cnt

        cnt += 1
        for i in arr[v]:
            if vis[i]:
                continue
            vis[i] = 1
            dfs(i)
    vis = [0] * (n+1)
    cnt = 0
    dfs(x[0])
    if cnt == n + 1:
        print("GOOD")
    else:
        print("BAD")

