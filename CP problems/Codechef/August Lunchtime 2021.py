import collections
import copy
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k= [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        dp = [0] * n

        max_a = max(a)
        for i in range(0, n):
            if a[i]== max_a:
                dp[i] += dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        cnt = 0

        for i in range(0, n-k+1):
            if a[i+k-1] == max_a:
                cnt += n - i - k + 1
        print(cnt)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        cnt_a = 0
        cnt_b = 0
        lo = []

        for i in range(0,n):
            lo.append(i - a[i])
        lo.sort()
        cnt = 1
        for i in range(0, n):
            if i == n - 1:
                if cnt > 1:
                    cnt_a += cnt
                else:
                    cnt_b += 1
                cnt = 1
                break
            if lo[i] == lo[i+1]:
                cnt += 1
            else:
                if cnt > 1:
                    cnt_a += cnt
                else:
                    cnt_b += 1
                cnt = 1

        res = (cnt_a)
        if cnt_b == 0:
            print(res)
        else:
            print(1)
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        lo = []
        for i in range(1, n):
            lo.append((a[i], i))
        lo.sort()
        lo.append((a[0],0))
        lo.reverse()

        if a[0] != max(a):
            print(-1)
        else:
            cnt = 0
            l = 0
            r = 0
            for i in range(1, n):

                if lo[i][1] > l:
                    cnt += 1
                    l = lo[i][1]
                else:
                    continue
            if l != n - 1:
                print(-1)
            else:
                print(cnt)

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

def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, m = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        sum_a = sum(a)
        left = [0] * n
        left[0] = a[0]
        right = [0] * n
        right[n-1] = a[n-1]
        for i in range(1,n):
            left[i] = left[i-1] + a[i]
        for i in range(n-2,0,-1):
            right[i] = right[i+1] + a[i]
        if sum_a % m == 0:
            print(0)
        else:
            cnt = 0

E()