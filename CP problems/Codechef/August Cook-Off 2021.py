import collections
import copy
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        ans = 0
        cnt = 1
        a.sort()
        for i in range(0, len(a)):
            if i == n - 1:
                ans = max(ans, cnt)
                break
            if a[i] == a[i+1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        if n <= 2:
            print(0)
        else:
            print(min(n-2, n-ans))

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = []

        for i in range(n):
            s1 = input()
            s.append(list(s1))
        res = []
        ans = True
        for i in range(n):
            s1 = []
            for j in range(0, n):
                if j == i:
                    s1.append('1')
                else:
                    s1.append('0')
            if s1 in s:
                ans = False
            else:
                res = s1
        if not ans:
            for i in range(n):
                s1 = []
                b = False
                for j in range(0, n):
                    if j == i:
                        s1.append('1')
                    else:
                        s1.append('0')
                for j in range(0, n):
                    if j == i:
                        continue
                    else:
                        s1[j] = '1'
                        if s1 in s:
                            s1[j] = '0'
                            continue
                        else:
                            res = s1
                            b = True
                            break
                if b:
                    break
            for i in res:
                print(i, end="")
            print()
        else:
            for i in res:
                print(i, end="")
            print()

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        freq = collections.Counter(a)
        res = n - freq[0] - freq[1] - freq[-1]
        if n - res <= 1:
            if n == 1:
                print(1)
            elif freq[-1] >= 1 and freq[1] == 0:
                if freq[0] == 0:
                    print(0)
                elif n - res == 1 and freq[-11] >= 1:
                    print(0)
                else:
                    print(1)
            elif n - res == 1 and freq[-1] >= 1:
                print(0)
            else:
                print(1)
        else:
            print(0)

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k ,x = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        res = sum(a)
        ans = sum(a)
        r = n - 1
        while k:
            ans -= (a[r] + a[r-1])
            ans += x
            r -= 2
            k -= 1
            res = min(res, ans)
        print(res)
C()