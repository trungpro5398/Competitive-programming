import bisect
from sys import stdin

def A():

    # Check if bitwise AND of any subset is power of two
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        dp = [0] * (max(a)+1)
        for i in a:
            dp[i] += 1
        res = n
        res = res * (res-1)
        for i in dp:
            if i > 1:
                res -= i *(i-1)
        print(res)
def B():
    t = int(stdin.readline())

    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        b = [int(x) for x in stdin.readline().split()]
        for i in range(len(a)):
            a[i] %= n
            b[i] %= n
        b.sort()
        for i in range(len(a)):
            sav = n - a[i]

            k = bisect.bisect_left(b, sav)
            print(k)


def C():
    t = int(stdin.readline())

    while t:
        t -= 1
        n , k , s = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        li = []
        cnt = 1
        res = 0
        for i in range(0, len(a)):
            res += a[i]
            if i == len(a)- 1 and res <= s:
                li.append(cnt)
            elif res == s:
                li.append(cnt)
                cnt = 1
                res = 0
            elif res + a[i+1] > s:
                li.append(cnt)
                cnt = 1
                res = 0
            else:
                cnt += 1
        res = 0
        l = 0
        sav = 0

        for i in range(0, len(li)):
            sav += li[i]
            res = max(res, sav)
            if i - l == k - 1:
                sav -= li[l]
                l += 1
            res = max(res, sav)
        print(res)



def D():
    t = int(stdin.readline())

    while t:
        t -= 1
def E():
    t = int(stdin.readline())

    while t:
        t -= 1


C()