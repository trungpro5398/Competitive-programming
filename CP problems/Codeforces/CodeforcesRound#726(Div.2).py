import math
from sys import stdin


def A():
    t = stdin.readline()
    t = int(t)

    while (t):
        e = stdin.readline()
        n = [int(x) for x in stdin.readline().split()]
        res = 0
        for i in n:
            res += i
        k = len(n)
        if res == k:
            print(0)
        else:
            if res <= 0 or res < k:
                print(1)
            else:
                print(res - k)
        t -= 1
def B():
    t = stdin.readline()
    t = int(t)

    while (t):
        t-=1
        a = [int(x) for x in stdin.readline().split()]
        n, m , i ,j = a[0], a[1], a[2], a[3]
        x1, y1, x2, y2 = 1, 1, n, m

        print(x1, y1, x2, y2)


def C():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        e = stdin.readline()
        n = [int(x) for x in stdin.readline().split()]
        n.sort()
        sav_a = 1
        if len(n) == 2:
            for i in n:
                print(i, end=' ')
            continue
        for i in range(2, len(n)):
            if n[i] - n[i-1] < n[sav_a] - n[sav_a-1]:
                sav_a = i
        res = []
        for i in range(sav_a, len(n)):
            res.append(n[i])
        for i in range(0, sav_a):
            res.append(n[i])

        for i in res:
            print(i, end=' ')
        print()
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
def D():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        n = int(stdin.readline())
        res = 0

        if n % 2 == 1:
            print("Bob")
        elif countSetBits(n) == 1:
            while n % 2 == 0:
                res += 1
                n /= 2
            if res % 2 == 1:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")

def E1():
    n = [int(x) for x in stdin.readline().split()]
    s = stdin.readline()
    s1 = s[0]
    for i in range(2, n[0]+1):
        s2 = s[0:i]
        if s2 + s1 < s1 + s2:
            s1 = s2
        print(s1)
    l = len(s1)
    for i in range(0, n[1]):
        print(s1[i%l], end="")




E1()