import collections
import copy
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k= [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        res = 0
        for i in range(0,n):
            if k > 0:
                res += abs(a[i])
                k -= 1
            elif a[i] < 0:
                continue
            else:
                res += a[i]
        print(res)
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        a.sort()
        b.sort()
        k = b[-1] - a[-1]
        k1 = b[-1] - a[-2]
        if k <= 0:
            print(k1)
        elif k1 <= 0:
            print(k)
        else:
            if a[0] + k == b[0] or a[1] + k == b[0]:
                if a[0] + k1 == b[0] or a[1] + k1 == b[0]:
                    print(min(k,k1))
                else:
                    print(k)
            else:
                print(k1)

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        res = a[0]
        for i in range(1,n):
            res &= a[i]
        cnt = 0
        lo = []
        for i in range(0,n):
            lo.append((b[i], i))
        lo.sort()
        lo.reverse()
        for i in range(0,n):
            if res == 0:
                res |= a[lo[i][1]]
                print(res)
                res &= lo[i][0]
                print(i, lo[i][0], lo[i][1])
                cnt += 1
            else:
                break
        print(res, cnt)
def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k ,x = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        res = sum(a)
        ans = sum(a)
        r = n - 1
        while k:
            ans -= (a[r] + a[r-1])
            ans += x
            r -= 2
            k -= 1
            res = min(res, ans)
        print(res)

def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, m = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        sum_a = sum(a)
        left = [0] * n
        left[0] = a[0]
        right = [0] * n
        right[n-1] = a[n-1]
        for i in range(1,n):
            left[i] = left[i-1] + a[i]
        for i in range(n-2,0,-1):
            right[i] = right[i+1] + a[i]
        if sum_a % m == 0:
            print(0)
        else:
            cnt = 0
print(1 ^2)
C()