import copy
import math
from sys import stdin


def A():
    t = stdin.readline()
    t = int(t)
    while t:
        t-=1
        s =input()
        cnt = 0
        cnt1 = 0
        cnt2 = 0
        for i in s:
            if i == 'A':
                cnt += 1
            if i =='B':
                cnt1 += 1
            if i == 'C':
                cnt2+= 1
        if cnt + cnt2 == cnt1:
            print("yes")
        elif cnt == cnt1 and 0 == cnt2:
            print("yes")
        elif cnt2 == cnt1 and cnt == 0:
            print("yes")
        else:
            print("NO")

def B():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = [int(x) for x in stdin.readline().split()]
        c = copy.deepcopy(a)
        c.sort()

        r = n + 1
        res = []

        for i in c:
            r -= 1

            for j in range(0, r):
                if a[j] == c[r-1]:
                    if min(n,j+1) == min(n,r) :
                        continue
                    res.append([ min(n, j + 1), min(n, r),1])

                    a.pop(j)

                    a.insert(r-1,c[r-1])
                    break

            if a == c:
                break
            if a[::-1] == c:
                break

        if a == c:
            print(len(res))
            for i in res:
                print("{} {} {}".format(i[0], i[1],i[2]))
        else:
            res.append([1,n,1])
            print(len(res))
            for i in res:
                print("{} {} {}".format(i[0], i[1],i[2]))

def D():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = [int(x) for x in stdin.readline().split()]
        lis = []
        for i in range(0, n):
            lis.append([a[i], i])
        lis.sort()
        l = 0
        r = len(a) - 1
        res = []
        while l < r:
            if lis[l][0] == 0:
                l += 1
            if lis[l][0] == 0:
                continue
            if lis[r][0] == 0:
                r -= 1
            if lis[r][0] == 0:
                continue
            if l == r:
                break
            res.append([lis[l][1] + 1,lis[r][1] + 1])
            lis[l][0] -= 1
            lis[r][0] -= 1
            if lis[r][0] < lis[r-1][0]:
                lis[r], lis[r-1] = lis[r-1], lis[r]
            if lis[l][0] < 0 or lis[r][0] <0:
                break
        print(len(res))
        for i in res:
            print("{} {}" .format(i[0], i[1]))

def E1():
    t = int(input())
    while t:
        t -= 1
        n =int(input())
        a = [int(x) for x in stdin.readline().split()]
        b = []
        b.append(a[0])
        for i in range(1, n):
            if a[i] > b[0]:
                b.append(a[i])
            else:
                b.insert(0,a[i])
        for i in b:
            print(i, end =" ")
        print()
D()