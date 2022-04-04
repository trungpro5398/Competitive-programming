import sys
from sys import stdin


def A():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        if a == b:
            print(0)
            continue
        res = []
        for i in range(0, n):
            if a[i] == b[i]:
                continue
            if a[i] < b[i]:
                for j in range(i + 1, n):
                    if a[i] == b[i]:
                        break
                    if a[j] > b[j]:
                        sav = min(b[i] - a[i], a[j] - b[j])
                        a[i] += sav
                        a[j] -= sav

                        for k in range(0, sav):
                            res.append((j,i))

            else:
                for j in range(i + 1, n):
                    if a[i] == b[i]:
                        break
                    if a[j] < b[j]:
                        sav = min(a[i] - b[i], b[j] - a[j])
                        a[i] -= sav
                        a[j] += sav

                        for k in range(0, sav):
                            res.append((i,j))

        if len(res) == 0 or a != b:
            print(-1)
        else:
            print(len(res))
            for i in res:
                print(i[0] + 1, end=" ")
                print(i[1] + 1, end= " ")
                print()

def B():
    t = int(stdin.readline())

    while t:
        t -= 1

        a = [int(x) for x in stdin.readline().split()]
        n, m = a[0], a[1]
        ABC = map(int, sys.stdin.buffer.read().split())
import copy

def C():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [0] * (max(a) + 1)
        c = [0] * (max(a) + 1)
        d = [0] * (max(a) + 1)
        e = [0] * (max(a) + 1)
        for i in a:
            b[i] += 1
        for i in range(0, len(a)):
            if b[a[i]] == 1:
                c[a[i]] = i
            else:
                if i % 2 == 0:
                    d[a[i]] += 1
        a.sort()
        res = True
        for i in range(0, len(a)):
            if b[a[i]] == 1:
                if c[a[i]] % 2 != i % 2:
                    res = False
                    break
            else:
                if i % 2 == 0:
                    e[a[i]] += 1
        for i in range(0, len(a)):
            if b[a[i]] == 1:
                continue
            else:
                if i % 2 == 0:
                    if e[a[i]] != d[a[i]]:
                        res = False
                        break
        if res:
            print("YES")
        else:
            print("NO")

C()