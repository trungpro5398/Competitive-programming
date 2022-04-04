import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1

        n, m = [int(x) for x in stdin.readline().split()]
        if n == 1 and m == 1:
            print(0)
        else:
            print(min(n,m))

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = []
        res1 = []
        l = 0
        r = n - 1
        while a[l] == a[r] and l < r:
            l += 1
            r -= 1
        for i in a:
            if i == a[l]:
                continue
            res.append(i)

        for i in a:
            if i == a[r]:
                continue
            res1.append(i)

        if res == res[::-1] or len(res) == 0:
            print("YES")
        elif res1 == res1[::-1] or len(res1) == 0:
            print("YES")
        else:
            print("NO")


def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [0] * n
        b = [0] * n
        for i in range(n):
            a[i], b[i] = [int(x) for x in stdin.readline().split()]
        l = []
        l.append((a[0], b[0]))
        res = 0
        for i in range(1, n):
            res = max(len(l), res)
            if b[i] < len(l):
                l.pop(0)
            elif a[0] < len(l):
                l.pop(0)
            l.append((a[i], b[i]))
            res = max(len(l), res)
        print(res)
def D():
    t = int(stdin.readline())
    while t:
        t -= 1


C()