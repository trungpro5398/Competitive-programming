from sys import stdin


def A():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        mod = 10 ** 9 + 7
        res = 1
        l = 3
        r = 4
        for i in range(1, n):
            res *= (l * r) % mod
            res %= mod
            l += 2
            r += 2
        print(res)


def B():
    t = int(input())
    while t:
        t -= 1
        n, m, k = [int(x) for x in stdin.readline().split()]
        if n == 1 and m == 0:
            print("YES")
        else:
            m *= 2
            m //= n
            m += 1
            m //= 2

            if n - m - 1< k - 1:
                print("YES")
            else:
                print("NO")

B()