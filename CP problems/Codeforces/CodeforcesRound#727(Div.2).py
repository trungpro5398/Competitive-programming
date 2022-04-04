import bisect
from math import ceil
from sys import stdin


def A():
    k = stdin.readline()
    k = int(k)

    while (k):
        k -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, x, t = a[0], a[1], a[2]
        cnt = min(t//x, n)
        res = max(0, n - cnt) * cnt + cnt * (cnt-1) // 2
        print(int(res))

def B():
    a = [int(x) for x in stdin.readline().split()]
    n, q = a[0], a[1]
    s = stdin.readline()
    res = [0] * ( n )
    res[0] = int(ord(s[0]) - 97 + 1)
    for i in range(1, n):
        res[i] = res[i-1] + int(ord(s[i]) - ord('a') + 1)

    while q:
        q -= 1
        b = [int(x) for x in stdin.readline().split()]
        l, r = b[0], b[1] - 1
        if b[0] == 1:
            print(res[r])
        else:
            print(res[r] - res[l-2])
def C():
    a = [int(x) for x in stdin.readline().split()]
    n, k ,x = a[0], a[1], a[2]
    a = [int(x) for x in stdin.readline().split()]
    a.sort()
    cnt = 0
    cnt1 = []
    for i in range(1, len(a)):
        if a[i] - a[i-1] > x:
            cnt += 1
            cnt1.append((a[i] - a[i-1] - 1) // x)
    cnt1.sort()
    l = 0
    while k and l < len(cnt1):

        if k < cnt1[l]:
            break
        k -= cnt1[l]
        l += 1
        cnt-=1

    print(cnt + 1)

C()