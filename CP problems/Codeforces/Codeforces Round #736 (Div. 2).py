import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        if n % 2 == 0:
            print(2, end=" ")
            print(int(n/2))
        else:

            print(2, end= " ")
            print(n-1)



def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = input()
        s1 = input()
        a = []
        b = []
        c = [0] * n
        for i in s:

            if i == '1':
                a.append(1)
            else:
                a.append(0)
        for i in s1:
            if i == '1':
                b.append(1)
            else:
                b.append(0)
        for i in range(len(a)):
            if i == 0:
                if b[i+1] == b[i] == 1:
                    c[i] = 1
                    b[i+1] = 0
                elif a[i] == a[i+1] and b[i+1] == 1:
                    c[i] = 1
                    b[i+1] = 0
            elif i == len(a) - 1:
                if b[i-1] == b[i] == 1:
                    c[i] = 1
                    b[i-1] = 0
                elif a[i] == a[i-1] and b[i-1] == 1:
                    c[i] = 1
                    b[i-1] = 0
            else:
                if b[i+1] == b[i] == 1:
                    c[i] = 1
                elif a[i] == a[i + 1] and b[i + 1] == 1:
                    c[i] = 1
                elif b[i-1] == b[i] == 1:
                    c[i] = 1
                elif a[i] == a[i - 1] and b[i - 1] == 1:
                    c[i] = 1

        print(min(c.count(1), b.count(1)))
def C():
    n, m = [int(x) for x in stdin.readline().split()]
    dp = [0] * (n+1)
    for i in range(m):
        u, v = [int(x) for x in stdin.readline().split()]
        dp[max(u, v)] = 1
    q = int(stdin.readline())
    for i in range(q):
        a = [int(x) for x in stdin.readline().split()]
        if a[0] == 1:
            if dp[min(a[1], a[2])] == dp[max(a[1], a[2])] == 0:
                dp[max(a[1], a[2])] = 1
        elif a[0] == 2:
            continue
        else:
            print(dp.count(1))



def D():
    t = int(stdin.readline())
    while t:
        t -= 1

C()

