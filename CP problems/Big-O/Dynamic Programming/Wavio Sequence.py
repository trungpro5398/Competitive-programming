
import bisect

def lis(a, dp):
    n = len(a)
    sub = [a[0]]
    for i in range(1,n):
        pos = bisect.bisect_left(sub, a[i])
        if pos == len(sub):
            sub.append(a[i])
        else:
            sub[pos] = a[i]
        dp[i] = pos + 1

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        ass = [0] * n
        des = [0] * n
        lis(a,ass)
        a.reverse()
        lis(a,des)
        ans = 1
        for i in range(n):
            sav = min(ass[i], des[n-i-1])
            ans = max(ans, 2 * sav - 1)
        print(ans)
    except:
        exit()