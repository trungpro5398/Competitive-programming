from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1

        a = [int(x) for x in stdin.readline().split()]
        w,h,n = a[0], a[1], a[2]
        cnt = 1
        cnt1 = 1
        while w % 2 == 0:
            w /= 2
            cnt *= 2
        while h % 2 == 0:
            h /= 2
            cnt1 *= 2
        if cnt * cnt1 >= n:
            print("YES")
        else:
            print("NO")

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        if sum(a) % 2 != 0:
            print("NO")
        else:
            sav = sum(a)
            res = True
            sav1 = sav / 2
            cnt = a.count(2)
            while cnt and sav1 > 1:
                sav1 -= 2
                cnt -= 1
            cnt1 = a.count(1)
            while cnt1 and sav1 > 0:
                sav1 -= 1
                cnt1 -= 1
            if cnt * 2 + cnt1 != sav // 2:
                res = False

            if res:
                print("YES")
            else:
                print("NO")
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        dp = [0] * n

        res = 0
        for i in range(n):
            s = i + a[i]
            if s < n:
                dp[s] = max(dp[s], dp[i] + a[i])
                res = max(res, dp[s])
            res = max(res, dp[i] + a[i])
        print(res)

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        a.reverse()
        sum = 0
        for i in range(n):
            if i % 2 == 0:
                if a[i] % 2 == 0:
                    sum += a[i]
            else:
                if a[i] % 2 == 1:
                    sum -= a[i]

        if sum == 0:
            print("Tie")
        elif sum > 0:
            print("Alice")
        else:
            print("Bob")


def E():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        q = [int(x) for x in stdin.readline().split()]

E()