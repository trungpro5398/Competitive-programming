from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        if n % 3 == 0:
            print(n // 3, end=" ")
            print(n // 3)
            continue
        sav = n // 3
        while (n-sav) % 2 != 0:
            sav += 1
        print(sav, end=" ")
        print((n-sav)//2)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        s = input()
        d = [0] * 27
        for i in s:
            c = ord(i) - ord('a')

            d[c] += 1
        cnt = 0
        cnt1 = 0
        for i in range(0,27):
            if d[i] == 0:
                continue

            if d[i] % 2 == 0:
                cnt += 1
            elif d[i] >= 3:
                cnt += 1
            else:
                cnt1 += 1
        print(cnt + cnt1//2)
def B1():
    t = int(stdin.readline())

    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        n, k = a[0], a[1]
        a = [int(x) for x in stdin.readline().split()]
        d = [0] * (max(a) + 2)

        for i in a:
            d[i] += 1
        cnt = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(0, len(d)):
            if d[i] == 0:
                continue
            if d[i] % k == 0:
                cnt += 1
            elif d[i] > k:
                cnt += 1

            else:
                cnt1 += d[i]

        cnt = cnt + cnt1 // k

        c = [0] * (max(max(a), k, n)  + 100)
        d = [1] * (max(max(a), k, n) + 100)
        e = [1] * (max(max(a), k, n) + 10)
        for i in a:
            c[i] += 1
        for i in a:
            while e[d[i]] > cnt:
                d[i] += 1

            if c[i] > 0 and e[d[i]] <= cnt and d[i] <= k:
                print(d[i], end= " ")
                e[d[i]] += 1
                d[i] += 1
                c[i] -= 1
            else:
                print(0, end= " ")
        print()

B1()