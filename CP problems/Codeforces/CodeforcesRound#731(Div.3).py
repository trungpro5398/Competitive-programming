from sys import stdin


def A():
    t = int(stdin.readline())

    while t:
        aaa= stdin.readline()
        t -= 1
        d = [int(x) for x in stdin.readline().split()]
        xa, ya = d[0], d[1]
        c = [int(x) for x in stdin.readline().split()]
        xb, yb = c[0], c[1]
        b = [int(x) for x in stdin.readline().split()]
        xf, yf = b[0], b[1]
        res = abs(xa-xb) + abs(ya-yb)
        if xa == xb  == xf and min(ya,yb) < yf < max(ya,yb):
            res += 2
        elif ya == yb == yf and min(xa,xb) < xf < max(xa,xb):
            res += 2
        print(res)
def B():
    t = int(stdin.readline())

    while t:
        s = input()
        t-= 1
        s1 = []
        for i in s:
            s1.append(ord(i) - ord('a'))
        sav = max(s1)
        l = 0
        r1 = len(s1) - 1
        res = True
        k = [0] * 30
        for i in s1:
            if k[i] > 1:
                res = False
                break
            k[i] += 1
        for i in k:
            if i > 1:
                res = False
                break
        if len(s1) > 1 and res:
            while sav == s1[l] or sav == s1[r1]:
                if sav == s1[l] == s1[r1]:
                    res = False
                    break
                if sav == s1[l]:
                    l += 1
                elif sav == s1[r1]:
                    r1 -= 1
                else:
                    res = False
                    break
                sav -= 1
                if sav <= 0 or l >= r1:
                    break
        if sav <= 0 and res:
            print("YES")
        else:
            print("NO")

def C():
    t = int(stdin.readline())

    while t:
        aaa = stdin.readline()
        t -= 1
        d = [int(x) for x in stdin.readline().split()]
        k,n,m = d[0], d[1], d[2]
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        l = 0
        l1 = 0
        res = []
        sav = True
        while l != n or l1 != m:
            if l != n and a[l] == 0:
                res.append(0)
                k += 1
                l += 1
            elif l1 != m and b[l1] == 0:
                res.append(0)
                k += 1
                l1 += 1
            elif l != n and a[l] <= k:
                res.append(a[l])
                l += 1
            elif l1 != m and b[l1] <= k:
                res.append(b[l1])
                l1 += 1
            else:
                print(-1)
                sav = False
                break
        if sav:
            for i in res:
                print(i, end = " ")
            print()
C()
