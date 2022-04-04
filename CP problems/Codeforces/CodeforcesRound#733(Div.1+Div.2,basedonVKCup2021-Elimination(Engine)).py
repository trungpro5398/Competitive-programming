from sys import stdin


def A():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        cnt = 0
        while (n > 0):

            # calculate m (A number
            # that has same number
            # of digits as n, but
            # has 1 in place of non-zero
            # digits 0 in place of 0 digits)
            temp = n;
            m = 0;
            p = 1;
            while (temp):
                rem = temp % 10;
                temp = int(temp / 10);

                if (rem != 0):
                    m += p;
                p *= 10;

            cnt += 1

            # subtract m from n
            n = n - m;

        print(cnt)

def B():
    t = int(stdin.readline())

    while t:
        t -= 1

        a = [int(x) for x in stdin.readline().split()]
        h, w = a[0], a[1]
        for i in range(h):
            for j in range(w):
                if (i == 0 or i == h-1) and j % 2 == 0:
                    print(1, end ="")
                elif i > 1 and i < h - 2 and i % 2 == 0 and ( j== 0 or j == w -1):
                    print(1, end="")
                else:
                    print(0, end="")
            print()
        print()
def C():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        cnt = 0
        sav = []
        for i in range(0, n):
            sav.append((b[i], a[i]))
        sav.sort()
        res = 0
        for i in range(0, n - n//4):
            res += sav[i][1]
        res1 = sum(b)
        if res == 0:
            print(1)
            continue
        cnt = res1 // res

        if res + cnt * 100 < res1:
            cnt += 1
        sav = []
        for i in range(0, n):
            sav.append((a[i], b[i]))
        sav.sort()
        sav.reverse()
        res = 0
        for i in range(0, n - n // 4):
            res += sav[i][0]
        res1 = sum(b)
        if res == 0:
            print(1)
            continue
        cnt1 = res1 // res

        if res + cnt1 * 100 < res1:
            cnt1 += 1

        print(min(cnt, cnt1))
def D():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = []
        for i in range(1, n+1):
            b.append(i)
        b.reverse()
        c = [0] * (n+1)
        C = [0] * (n + 1)
        k = 0
        for i in a:
            if c[i] == 0:
                k += 1
            c[i] = 1
        d = [0] * (n)

        for i in range(n):

            if c[a[i]] == 1 :
                d[i] = a[i]
                c[a[i]] = 0
                C[a[i]] = 1
            else:
                d[i] = 0
        l = 1
        for i in range(n):
            if d[i] == 0:
                while C[l]:
                    l += 1
                d[i] = l
                l += 1
        r = [0] * (n + 1)
        for i in range(0, n):
            r[d[i]] = i
        for i in range(0, n):
            if d[i] == i + 1:
                d[i], d[r[a[i]]] = d[r[a[i]]], d[i]
                

        print(k)
        for i in d:
            print(i, end=" ")
        print()
D()