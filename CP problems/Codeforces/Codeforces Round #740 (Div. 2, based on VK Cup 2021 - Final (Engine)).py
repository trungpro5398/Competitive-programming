import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = copy.deepcopy(a)
        b.sort()
        if a == b:
            print(0)
        else:
            i = 1
            while a != b:
                if i % 2 == 0:
                    for j in range(0, n):
                        if (j + 1) % 2 == 0:
                            if j < n - 1:
                                if a[j] > a[j + 1]:
                                    a[j], a[j + 1] = a[j + 1], a[j]
                else:
                    for j in range(0, n):
                        if (j + 1) % 2 == 1:
                            if j < n - 1:
                                if a[j] > a[j + 1]:
                                    a[j], a[j + 1] = a[j + 1], a[j]
                i += 1
            print(i - 1)


def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        a, b = [int(x) for x in stdin.readline().split()]
        total = a + b


def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        ans = 0
        dp = [0] * n
        dp1 = [0] * n
        dp2 = [0] * n
        dp3 = [0] * n
        dp4 = [0] * n
        cnt1 = 0
        for i in range(0, n):
            a = [int(x) for x in stdin.readline().split()]
            ans = a[1] + a[0]
            for j in range(2, len(a)):
                cnt1 += 1
                if ans <= a[j]:
                    ans = a[j] - j + a[0] + 1
            dp[i] = ans - a[0] + 1
            dp1[i] = ans
            dp2[i] = ans - a[0] + 1
            dp3[i] = ans
            dp4[i] = a[0] - 1
            cnt1 += 1
        dp2.sort()
        k = 0
        for i in range(0, len(dp)):
            if dp[i] == dp2[-1]:
                k = max(k, dp4[i])
        dp3.sort()
        ans = 0
        for i in range(0, len(dp3)):
            dp3[i] += cnt1
        for i in dp3:
            if i - k >= dp2[-1]:
                ans = i
                break
        cnt = 10 ** 9

        for i in range(0, n):
            if dp1[i] == ans - cnt1:
                cnt = min(cnt, dp1[i] - dp4[i])
        print(cnt)


def D():
    n, m = [int(x) for x in stdin.readline().split()]
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    cnt = 3
    for i in range(3, n + 1):
        dp[i] += (cnt + i - i // 2) % m
        for j in range(2, i // 2 + 1):
            dp[i] += dp[i // j] % m

        dp[i] %= m
        cnt += dp[i]
        cnt %= m
    print(dp)


def F1():
    t = int(stdin.readline())
    while t:
        t -= 1


D()