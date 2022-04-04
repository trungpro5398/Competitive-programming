import bisect
from collections import defaultdict, deque
from sys import stdin


def A():
    t = int(stdin.readline())

    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, m, x = a[0], a[1], a[2]
        l = 1
        cnt = x // n

        if cnt * n < x:
            l = cnt * n + 1
            cnt += 1
        else:
            l = cnt * n - n + 1

        cnt1 = x - l + 1

        res  = cnt + (cnt1-1) * m
        print(res)


def B():
    t = int(stdin.readline())

    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, k = a[0], a[1]
        s = stdin.readline()
        cnt = 1
        l = 0
        for i in range(len(s)):
            if s[i] == '*':
                l = i
                break
        while True:
            j = min(n-1, l + k)
            while l < j and s[j] =='.':
                j -=1
            if l == j:
                break
            cnt += 1
            l = j
        print(cnt)




def C():
    t = int(stdin.readline())

    while t:
        t -= 1
        a = stdin.readline()
        b = stdin.readline()
        ans = 0
        for i in range(1, min(len(a), len(b))):
            for j in range(len(a)-i ):
                for k in range(len(b)-i):
                    if a[j: j + i] == b[k: k + i] :
                        ans = max(ans, i)

        print(max(len(a) + len(b) - 2 * ans - 2,0))

def D():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = 0
        mp = defaultdict(lambda: 0)
        for i in range(0, len(a)):
            mp[a[i]] += 1
            res = max(res, mp[a[i]])
        sav = 0
        if n & 1:
            sav = 1
        print( max(sav, 2 * res - n))


def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        q = [int(x) for x in stdin.readline().split()]
        d = [0] * (n+1)
        d1 = [0] * (n+1)
        l = 1
        for i in range(0, n):
            if d1[q[i]] == 0:
                d[i] = q[i]
                d1[q[i]] = 1
            else:
                while d1[l] != 0 and l <= n:
                    l += 1
                d[i] = l
                d1[l] = 1
                l += 1
        for i in range(0, n):
            print(d[i], end=" ")
        print()
        d = []
        s = deque()
        a = 0
        for i in range(1,n+1):
            s.append(i)
        for i in range(0, n):
            c = q[i]
            if c == a:
                d.append(s.pop())
            else:
                d.append(c)
                for i in range(a+1,c):
                    s.append(i)
                a = c

        for i in range(0, n):
            print(d[i], end=" ")
        print()

s = "abcdef"
s[3] ='r'
print(s[0:8])