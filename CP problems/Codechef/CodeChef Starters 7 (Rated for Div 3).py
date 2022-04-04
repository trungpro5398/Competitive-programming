import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        x = [int(x) for x in stdin.readline().split()]
        a, b = x[0], x[1]
        if a + b < 3:
            print(1)
        elif 3 <= a + b <= 10:
            print(2)
        elif 11 <= a+ b <= 60:
            print(3)
        else:
            print(4)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        x = [int(x) for x in stdin.readline().split()]
        e, k = x[0], x[1]
        cnt  = 0
        while e // k:
            e //= k
            cnt += 1
        print( cnt + 1)

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        x = [int(x) for x in stdin.readline().split()]
        n, k = x[0], x[1]
        res = ( 2 ** n ) ^ (2 ** n - 1)
        ans = (2**n) // 2
        res *= min(ans,k)
        print(max(0, res - min(ans,k)))

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        x = [int(x) for x in stdin.readline().split()]
        a, b = x[0], x[1]
        if a > b:
            sav = b - (b + 1)
            sav /= 2
            sav1 = (b+1) - a
            sav1 /= 2
            print(math.ceil(sav) + math.ceil(sav1))
        elif a== b:
            print(0)
        else:
            sav = b - (a+1)
            sav /= 2

            print(math.ceil(sav)+1)
C()