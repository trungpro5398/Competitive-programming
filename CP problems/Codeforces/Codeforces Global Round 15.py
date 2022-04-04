import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = input()
        s1 = copy.deepcopy(s)
        s1 = list(s1)
        s1.sort()

        s = list(s)
        cnt = 0
        for i in range(0, len(s)):
            if s[i] != s1[i]:
                cnt += 1
        print(cnt)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        b = [0] * 5
        b[0],b[1],b[2],b[3],b[4] = 500005,500005,500005,500005,500005
        sav = -1
        cols = 5
        rows = n
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(n):
            a = [int(x) for x in stdin.readline().split()]
            for j in range(5):
                arr[i][j] = a[j]
            b[0] = min(b[0],a[0])
            b[1] = min(b[1], a[1])
            b[2] = min(b[2], a[2])
            b[3] = min(b[3], a[3])
            b[4] = min(b[4], a[4])
        res = -1
        print(b)
        for i in range(n):
            cnt = 0
            for j in range(5):
                if arr[i][j] <= b[j]:
                    cnt += 1
            if cnt >= 3:
                res = i + 1
                break
        if res != -1:
            print(res)
        else:
            print(-1)
def countMaxIntersect(n):
    return int(n*(n - 1)/2)
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, k = a[0], a[1]

        res = countMaxIntersect(n-k)
        for i in range(k):
            a = [int(x) for x in stdin.readline().split()]
            k = min(a[0],a[1])
            k1 = max(a[1],a[0])
            k2 = max(0,k1 - k - 1)
            k3 = max(0,k - 1)
            print(k2,k3)
            res += min(k2,k3)
        print(res)



def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        res = False
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        print(a)
        for i in range(n):
            dp = [0] * n
            c = True
            for j in range(n):
                if j != i:
                    dp[j] = a[j]
            b = False
            for k in range(n):
                for k1 in range(n):

                    if a[i] == dp[k] - dp[k1]:
                        b = True
                        break

            if b == False:
                c = False
            if c:
                res = True
                break
        if res:
            print("YES")
        else:
            a.sort()
            dp = [0] * n
            b = False
            dp[0] = a[0]
            for i in range(1, n):
                dp[i] = a[i] + dp[i-1]
            for k in range(n):
                for k1 in range(n):

                    if a[0] == dp[k] - dp[k1]:
                        b = True
                        break
            print(dp)
            if b == False:
                print("NO")
            else:
                print("YES")


def E():
    t = int(stdin.readline())
    while t:
        t -= 1

D()