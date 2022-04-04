
import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [6,8,10]
        b = [15,20,25]
        res = 10 ** 17
        for i in range(3):
            sav = n // a[i]
            sav1 = sav * a[i]
            if sav1 < n:
                sav += 1
            res = min(res, sav * b[i])

        print(res)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        W, H = a[0], a[1]
        a = [int(x) for x in stdin.readline().split()]
        x1, y1, x2, y2 = a
        w, h = [int(x) for x in stdin.readline().split()]
        w1 = abs(x1-x2)
        h1 = abs(y1-y2)

        if w + w1 > W and h + h1 > H:
            print(-1)
        else:
            if w + w1 > W:
                if h > y1 and h > y2:
                    print(min(abs(h-y1),abs(h-y2)))
                else:
                    print(h-y1)
            elif h + h1 > H:
                if w > x1 and w > x2:
                    print(min(abs(w-x1), abs(w-x2)))
                else:
                    print(w-x1)
            else:
                if h > y1 and h > y2 and w > x1 and w > x2:
                    print(min(abs(h-y1),abs(w-x2),abs(w-x1), abs(h-y2)))
                else:
                    print(min(h-y1,w-x1))

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
def D():
    t = int(stdin.readline())
    while t:
        t -= 1


B()