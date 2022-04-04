from sys import stdin


def lower_bound(a, sub, n, x):
    left = 0
    right = n
    pos = right

    while  left < right:
        mid = left + (right - left) // 2
        index = sub[mid]

        if a[index][1] >= x:
            pos = mid
            right = mid
        else:
            left = mid + 1
    return pos

def lis(a):
    global path
    length = 1
    path = [-1] * len(a)
    dp = []
    dp.append(0)
    for i in range(1, len(a)):
        if a[i][1] <= a[dp[0]][1]:
            dp[0] = i
        elif a[i][1] > a[dp[length-1]][1]:
            path[i] = dp[length-1]
            dp.append(i)
            length += 1
        else:
            pos = lower_bound(a,dp, length, a[i][1])
            path[i] = dp[pos-1]
            dp[pos] = i
    res = []
    i = dp[length-1]
    while i >= 0:
        res.append(a[i][2])
        i = path[i]
    return length, res

n = int(input())
lo = []
for i in range(n):
    a = [int(x) for x in stdin.readline().split()]
    lo.append((a[0],a[1],i+1))

lo.sort(key=lambda x:(x[0],-x[1]))

ans,res = lis(lo)
print(ans)
for i in reversed(res):
    print('{} '.format(i),end = '')
