import bisect
from sys import stdin


def A():
    def g(l,r, t):
        global res, n
        if len(res) == n:
            return
        if l == r == 0:
            res.append(t)
            return
        if l > 0:
            g(l-1,r, t + '(')
        if r > l:
            g(l, r-1, t + ')')
    t = int(stdin.readline())
    while t:
        t -= 1
        global res, n
        n = int(input())

        res = []
        g(n,n,"")
        for i in range(0, n):
            print(res[i])


def B():
    t = int(stdin.readline())
    while t:
        t-=1
        a,b,c , m = [int(x) for x in stdin.readline().split()]




def C():
    n =int(input())
    a = [int(x) for x in stdin.readline().split()]
    m = int(input())
    a.sort()
    total = sum(a)
    for i in range(m):
        x, y = [int(x) for x in stdin.readline().split()]
        k = bisect.bisect_left(a,x,0,n)
        k = min(n-1,k)
        if a[k] > x:

            k2 = abs(a[k-1] - x)
            k3 = total - a[k]
            k4 = total - a[k-1]
            k3 = y - k3
            k4 = y - k4
            res_1 = max(0, k3)
            res_2 = max(0, k4) + k2
            print(min(res_1,res_2))
        else:
            k2 = min(0,a[k] - x)
            k4 = total - a[k]
            k4 = y - k4
            res_2 = max(0, k4) - k2
            print(res_2)

def D():
    n = int(input())
    a = [int(x) for x in stdin.readline().split()]

D()