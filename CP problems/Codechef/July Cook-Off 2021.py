import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        x, y = a[0], a[1]
        sav = math.gcd(x,y)
        if sav > 1:
            print(0)
        else:
            cnt = 0

            sav = math.gcd(x+1, y)
            sav1 = math.gcd(x, y+1)
            if sav > 1 or sav1 > 1:
                print(1)
            else:
                print(2)
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        sav = a[len(a)-1]
        for i in range(len(a)):
            a[i] ^= a[len(a)-1]

        res = 0
        for i in a:
            res |= i
        print(sav, end=" ")
        print(res)
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        dp = [0] * (max(a)+1)
        dp1 = [0] * (max(a) + 1)
        for i in a:
            dp[i] += 1
        for i in a:
            dp1[i] = i - 1
        res = 0
        for i in a:
            if dp1[i] > 0:
                res += 1
                dp1[i] -= 1
        print(res)
def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        if a[0] == 0:
            cnt = a.count(a[0])
            print(n - cnt)
        else:
            cnt = a.count(a[0])
            dp = [0] * 3

            for i in a:
                if i == 1 or i == 2:
                    dp[i] = 1

            if dp[1] and dp[2]:
                print(n)
            else:

                k1 = 0
                cnt1 = 0
                if a[0] % 2 == 0:
                    cnt1 += 1
                for i in range(0, len(a)):
                    if a[i] - a[0] == 1:
                        k1 = 1
                    if a[i] > a[0] and a[i] % 2 == 0 and a[0] % 2 == 0:
                        cnt1 += 1
                if cnt1 >= 2:
                    k1 = 1
                if k1:
                    print(n)
                else:
                    print(n - cnt)

def E():
    t = int(stdin.readline())
    while t:
        t -= 1

D()