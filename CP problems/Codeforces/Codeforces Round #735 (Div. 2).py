import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = 0
        for i in range(0, len(a)-1):
            res = max(res, a[i] * a[i+1])
        print(res)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, k = a[0], a[1]
        a = [int(x) for x in stdin.readline().split()]
        def f(a, l, r):
            return l * r - k * (a[l-1] | a[r-1])
        res = -(10**10)

        for i in range(0, len(a)-1):
            res = max(res, f(a, i+1, i+2))
        print(res)
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n,m = a[0], a[1]
        m1 = copy.deepcopy(m)
        m += 1
        res =  n ^ m

        while res >= m1:
            m += 1
            res = n ^ m
        while n ^ m < m1:
            m += 1
            res = min(n ^ m, res)

        print(res)
def D():
    t = int(stdin.readline())
    while t:
        t -= 1

print(bin(69))
C()