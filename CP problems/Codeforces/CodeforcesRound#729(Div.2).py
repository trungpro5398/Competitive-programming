import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b= []
        c= []
        for i in a:
            if i % 2:
                b.append(i)
            else:
                c.append(i)
        if len(b) == len(c):
            print("Yes")
        else:
            print("No")
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        d = [int(x) for x in stdin.readline().split()]
        n, a, b = d[0], d[1], d[2]
        if a == 1:
            if (n-1) % b == 0:
                print("YES")
            else:
                print("NO")
        else:
            k = 1
            sav = False
            while k <= n:
                if k % b == n % b :
                    sav = True
                    break
                k *= a
            if sav:
                print("YES")
            else:
                print("NO")
def lcm(a,b):
    return int(a * b / math.gcd(a,b))
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        res = 0
        g = 1
        for i in range(1,n+1):
            g = lcm(g,i)

            if g > n:
                break
            res += n // g
        print((res + n) % (10**9+7))

C()