from sys import stdin


def A():
    t = int(input())
    while t:
        t -= 1
        s = input()
        s1 = input()
        dp = [0] * 26
        for i in range(0, len(s)):
            dp[ord(s[i]) - ord('a')] = i
        ans = 0
        for i in range(0, len(s1) - 1):
            ans += abs(dp[ord(s1[i+1]) - ord('a')] - dp[ord(s1[i]) - ord('a')])
        print(ans)
A()
def B():
    t = int(input())
    while t:
        t -= 1
        x, n = [int(x) for x in stdin.readline().split()]
        k = n // 4 * 4 + 1
        for i in range(k, n+1):
            if x & 1:
                x += i
            else:
                x -= i
        print(x)

def C():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        x = [int(x) for x in stdin.readline().split()]
        x.sort()
        ans = x[0]
        for i in range(0, n-1):
            ans = max(ans, x[i+1] - x[i])
        print(ans)

def D():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        x = [int(x) for x in stdin.readline().split()]
        s = input()
        l, r = [], []
        for i in range(0, n):
            if s[i] == 'B':
                l.append(x[i])
            else:
                r.append(x[i])
        l.sort()
        r.sort()
        r.reverse()
        ans = True
        for i in range(0, len(l)):
            if l[i] < i + 1:
                ans = False
        for i in range(0, len(r)):
            if r[i] > n - i:
                ans = False
        if ans:
            print("yes")
        else:
            print("no")
D()