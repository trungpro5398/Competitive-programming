import itertools
import math
from sys import stdin


def A():
    a =[int(x) for x in stdin.readline().split()]
    n = a[0]
    print(int(n * (n/2)))

def B():
    t = int(input())
    while t:
        t -= 1
        b = [int(x) for x in stdin.readline().split()]
        n, a = b[0], b[1]
        res = 0
        for i in range(n, -1, -1):
            if math.sqrt(i) * math.sqrt(i) == i:
                res = max(res, int(math.sqrt(i)) * a)
                break
        print(res)

def C():
    t = int(input())
    while t:
        t -= 1
        b = [int(x) for x in stdin.readline().split()]
        n,m,q = b[0], b[1], b[2]
        res = True
        cnt = 0
        dp = [0] * (n+1)
        cnt = 0
        while q:
            q -= 1
            b = input().split()
            i = int(b[1])
            if b[0] == '+':
                if dp[i] == 1:
                    res = False
                dp[i] = 1
                cnt += 1
            else:
                if dp[i] == 0:
                    res= False
                dp[i] = 0
                cnt -= 1
            if cnt > m:
                res = False
        if res:
            print("Consistent")
        else:
            print("Inconsistent")
def D():
    t = int(input())
    while t:
        t -= 1
        n, k = [int(x) for x in stdin.readline().split()]
        s = input()
        pos = []
        for i in range(0, len(s)):
            if s[i] =='1':
                pos.append(i)

        cnt = 1
        if len(pos) == 0:
            cnt = 0
        if len(pos) > 0:
            pos[0] += 1
        for i in range(1, len(pos)):
            if pos[i] - pos[i-1] == k:
                continue
            if pos[i] - pos[i-1] < k:
                pos[i] += 1
            elif pos[i] - pos[i-1] <= k + 1:
                pos[i] -= 1
            else:
                pos[i] += 1
                cnt += 1
        print(cnt)

def E():
    mod = 1000000007
    f = [0] * (10**5+10)
    f1 = [0] * (10**5+10)
    f[0] = 0
    f[1] = 1
    f1[0] = 1
    f1[1] = 1
    def power(base, pow):
        res = 1
        while pow:
            if pow & 1:
                res *= base
            pow >>= 1
            base *= base
            base %= mod
            res % mod

        return res
    for i in range(2, 10**5+10):
        f[i] = (f[i-1] + f[i-2]) % mod
        f1[i] = (f1[i-1] + f1[i-2]) % (mod - 1)


    t = int(input())

    while t:
        t -= 1
        n = int(input())
        ans = (f[n] * power(2, f1[n]-1)) % mod
        print(ans)


E()