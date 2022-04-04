import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = stdin.readline()
        a = [0] * 1000
        res = True
        s1 = []
        for i in range(0, n):
            sav = ord(s[i]) - ord('A')
            if s[i] != s[i+1]:
                s1.append(s[i])


        for i in s1:
            sav = ord(i) - ord('A')
            if a[sav] == 0:
                a[sav] = 1
            else:
                res = False
        if res:
            print("yes")
        else:
            print("no")

def B():
    t = int(stdin.readline())
    f = [1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111]
    while t:
        t -= 1
        n = int(stdin.readline())
        if n <= 9:
            print(n)
            continue

        for i in range(0, len(f)):
            if f[i] - 1 == n:
                sav = n // f[i]
                res = i * 9 + sav
                print(res)
                break
            if f[i] > n:
                sav = n // f[i-1]
                res = (i-1) * 9 + sav
                print(res)
                break
            if f[i] == n:
                sav = n // f[i]
                res = i * 9 + sav
                print(res)
                break

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        if n % 2 == 0:
            print(-1)
        else:
            l = 1
            for i in range(0, n):
                for j in range(0, n, 2):
                    if j == n - 1:
                        print(l)
                        break
                    print(l+1, end= " ")
                    print(l, end=" ")
                    l += 2
def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = []
        res2 = []

        for i in range(0, len(a)):
            a[i] -= i
        d = [0] * (max(max(a) , -min(a))+ 1)
        e = [0] * (max(max(a) , -min(a))+ 1)
        for i in a:
            if i < 0:
                i = -i
                e[i] += 1
                if e[i] == 2:
                    res2.append(i)
            else:
                d[i] += 1
                if d[i] == 2:
                    res.append(i)


        res1 = 0

        for i in res:
            res1 += d[i] * (d[i]-1) / 2
        for i in res2:
            res1 += e[i] * (e[i]-1) / 2
        print(int(res1))
def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = stdin.readline()
        s1 = []
        d = [0] * n
        for i in range(0, len(s)):
            if s[i] == '*':
                s1.append(i+1)
        sav = sum(s1)
        res = 10**11
        if len(s1) > 0:
            d[0] = s1[0]
        for i in range(1, len(s1)):
            d[i] += d[i-1] + s1[i]

        for i in range(0, len(s1)):
            l = i + 1
            r = len(s1) - i - 1
            sav1 = s1[i] * l - s1[i] * r
            sav3 = sav - d[i]
            sav2 = sav1 - d[i] + sav3 - l * (l-1) / 2 - r * (r+1)/ 2
            res = min(res, sav2)
        if res == 10 ** 11:
            print(0)
        else:
            print(int(res))

E()