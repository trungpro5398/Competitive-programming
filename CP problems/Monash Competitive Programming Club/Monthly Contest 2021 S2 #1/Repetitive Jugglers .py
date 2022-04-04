import math
from sys import stdin


n = int(stdin.readline())

a = [int(x) for x in stdin.readline().split()]


for i in range(0, len(a)):
    a[i] -= 1

cnt = 0

adj = [[] for _ in range(n)]
for i in range(0, n):
    adj[i].append(a[i])

vis = [False] * n
bool = True
res = []
for i in range(0, n):
    if not vis[i]:
        start = i
        vis[i] = True
        queue = []
        queue.append(i)
        cnt = 0
        cycle = False
        while queue:
            v = queue.pop(0)
            cnt += 1
            vis[v] = True

            for j in adj[v]:
                if j == start:
                    cycle = True
                    break
                if not vis[j]:
                    queue.append(j)
            if cycle:
                break
        if not cycle:
            bool = False
            break
        res.append(cnt)

if not bool:
    print(-1)
else:
    cnt = 1

    def lcm(c , d ):
        return int(c * d / math.gcd(c,d))

    for i in res:
        cnt = lcm(cnt, i)
    print(cnt)

