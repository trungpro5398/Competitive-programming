import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        cnt  = 0
        k = int(stdin.readline())
        i = 0
        while True:
            if i % 3 == 0 or i % 10 == 3:
                i+= 1
                continue
            cnt += 1
            if cnt == k:
                break
            i += 1
        print(i)
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        a, b ,c  = [int(x) for x in stdin.readline().split()]
        k = abs(b - a)
        k1 = c + k

        if  k * 2 < max(a,b,c):
            print(-1)
        elif k1 > k * 2:
            k1 = c - k
            if k1 >= 0:
                print(k1)
            else:
                print(-1)
        else:
            print(k1)

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        k1 = copy.deepcopy(a[0])
        k = math.sqrt(a[0])
        if int(k) ** 2 == k1:
            print("{} {}".format(int(k), 1))
        else:
            top = int(math.ceil(k))

            if top * top - top + 1 <= k1 <= top * top:
                print("{} {}".format(top, top*top - k1+1))
            else:
                print("{} {}".format( k1 - (top-1)**2, top))


def D():
    t = int(stdin.readline())

    r = [str(2 ** i) for i in range(60)]
    def min_dif(x, s):
        cnt = 0
        for i in x:
            if i == s[cnt]:
                cnt += 1
                if cnt == len(s):
                    break
        return len(x) + len(s) - 2 * cnt
    for i in range(t):
        n = input()
        print(min([min_dif(n, i) for i in r]))

def F1():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k = input().split()
        n = list(n)
        k = int(k)
        if k == 1:

            for i in range(1, len(n)):
                if n[i] > n[0]:
                    n[0] = n[i]
            for i in n:
                print(n[0], end='')
        else:
            if len(n) <= 2:
                for i in n:
                    print(i, end="")
            else:
                l = 1
                n = list(n)
                for i in range(1, len(n)):
                    if n[i] == n[0]:
                        l += 1
                    else:
                        break

                if l >= len(n)-1:
                    for i in n:
                        print(i, end='')
                elif l < len(n) and n[l] < n[0]:
                    for i in range(l, len(n)):
                        n[i] = n[0]
                    for i in n:
                        print(i, end='')
                else:

                    l1 = copy.deepcopy(l)

                    if l1 >= len(n) - 1:
                        for i in n:
                            print(i, end='')
                        continue

                    maxans = max(n[l1+1:-1])

                    if maxans == n[l1]:
                        for i in range(l1, len(n)):

                            n[i] = n[l1]
                        for i in n:
                            print(i, end='')
                    elif maxans <= n[0]:
                        for i in range(l1+1, len(n)):
                            n[i] = n[0]
                        for i in n:
                            print(i, end='')
                    else:
                        for i in range(0, min(l1, len(n))):
                            print(n[0], end="")
                        if l1 < len(n):
                            print(ord(n[l1]) - ord('0') + 1, end="")
                            for i in range(l1 + 1, len(n)):
                                print(n[0], end="")

        print()

D()