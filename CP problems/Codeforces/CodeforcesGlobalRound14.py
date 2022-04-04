import copy
import math
from sys import stdin


def A():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1

        a = [int(x) for x in stdin.readline().split()]
        n, x = a[0], a[1]
        w = [int(x) for x in stdin.readline().split()]
        w.sort()
        res = 0
        res_b = True
        for i in range(0, n):
            res += w[i]
            if res == x:
                l = i
                while res == x:
                    if l >= n:
                        res_b = False
                        break
                    res -= w[l]
                    l += 1
                    if l >= n:
                        res_b = False
                        break
                    res += w[l]
                if l >= n:
                    res_b = False
                    break
                w[i], w[l] = w[l], w[i]
        if res_b:
            print("YES")
            for i in w:
                print(i, end=" ")
            print()
        else:
            print("NO")

def sq(c):
    d = int(math.sqrt(c))

    if d * d == c:
        return 1
    return 0
def B():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        b = int(stdin.readline())
        res = True
        if ( b % 2 == 0 and sq(b/2)) or ( b%4 == 0 and sq(b/4)):
            print( "YES")
        else:
            print("NO")
import heapq


def C():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        b = [int(x) for x in stdin.readline().split()]
        n, m, x = b[0], b[1], b[2]
        h = [int(x) for x in stdin.readline().split()]

        mat = []
        print("YES")
        for i in range(1, m+1):
            heapq.heappush(mat, (0, i))
        for i in range(0, len(h)):
            rs, pos = heapq.heappop(mat)
            print(pos, end= " ")
            heapq.heappush(mat, (rs + h[i], pos))

def D():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        b = [int(x) for x in stdin.readline().split()]
        n, l, r = b[0], b[1], b[2]
        c = [int(x) for x in stdin.readline().split()]
        left = []
        right = []
        for i in range(0, l):
            left.append(c[i])
        for i in range(l, n):
            right.append(c[i])
        l = 0
        left.sort()
        right.sort()
        res = 0
        if len(left) != len(right):
            res += int(abs(len(left) - len(right))/2)
            while len(left) < len(right):
                sav = len(right)-1
                do = True
                for i in range(0, len(right)-1):
                    if right[i] == right[i+1]:
                        sav = right.pop(i)
                        do = False
                        break
                if len(left) == len(right):
                    break
                if do == True:
                    right.pop(len(right)-1)
                left.append(sav)
            left.sort()
            right.sort()
            while len(left) > len(right):
                sav = len(left) - 1
                do = True
                for i in range(0, len(left) - 1):
                    if left[i] == left[i + 1]:
                        sav = left.pop(i)
                        break
                if len(left) == len(right):
                    break
                if do == True:
                    left.pop(len(left) - 1)
                right.append(sav)

        left.sort()
        right.sort()
        for i in range(0, len(left)):
            if left[i] != right[i]:
                res += 1
        print( c, left, right, res)



D()

