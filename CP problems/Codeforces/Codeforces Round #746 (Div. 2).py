import copy
from sys import stdin


def A():
    t = int(input())
    while t:
        t -= 1
        n, h  = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        temp = a[-1] + a[-2]
        if h < a[-1] or h < a[-2]:
            print(1)
        else:
            k = h // temp
            if h - k * temp > a[-1]:
                print(k * 2 + 2)
            elif h - k * temp > 0 :
                print(k * 2 + 1)
            else:
                print(2*k)



def B():
    t = int(input())
    while t:
        t -= 1
        n, x = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        arr = [[] for j in range(n + 1)]
        global vis, cnt
        def dfs(v):
            global vis, cnt

            cnt += 1
            for i in arr[v]:
                if i in vis:
                    continue
                vis[i] = 1
                dfs(i)

        vis = {}
        cnt = 0
        lis = []
        for i in range(0, n):
            lis.append([a[i], i+1])
        lis.sort()
        for i in range(n):

            arr[lis[i][1]].append(i+1)
        dfs(a[0])
        if cnt == n + 1 and x <= n // 2:
            print("YES")
        else:
            b = copy.deepcopy(a)
            b.sort()
            if b == a:
                print("YES")
            else:
                print("NO")

B()