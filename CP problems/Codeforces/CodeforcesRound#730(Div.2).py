import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        d = [int(x) for x in stdin.readline().split()]
        a, b = d[0], d[1]
        gcd = math.gcd(a,b)
        if gcd == a == b:
            print(0, end= " ")
            print(0)
        else:
            g = abs(a-b)
            m = min(a % g, g - a % g)
            print(g, end = " ")
            print(m)
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = sum(a) % n
        sav = sum(a) // n
        print(res * (n-res))
print(112//111)