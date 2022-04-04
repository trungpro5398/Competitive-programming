import queue
import sys
from sys import stdin






n = int(input())
adj = [[] for _ in range(n+1)]
vis = [0] * (n+1)
st = [0] * (n+1)
ed = [0] * (n+1)
time = 0

for i in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(cnt):
    global st,time, ed,vis
    vis[cnt] = 1
    st[cnt] = time
    time += 1
    for i in adj[cnt]:
        if vis[i] ==0:
            dfs(i)
    ed[cnt] = time
    time += 1
# recursion nho set limit
sys.setrecursionlimit(10**7)
dfs(1)
q = int(input())

def check(x, y):

    if st[x] > st[y] and ed[x] < ed[y]:
        return True
    return False
while q:
    q -= 1
    a,x, y = [int(x) for x in stdin.readline().split()]

    if not check(x,y) and not check(y,x):
        print("NO")
        continue
    if a == 0:
        if check(y,x):
            print("YES")
        else:
            print("NO")
    else:
        if check(x,y):
            print("YES")
        else:
            print("NO")