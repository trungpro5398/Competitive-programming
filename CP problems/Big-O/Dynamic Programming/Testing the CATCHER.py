
def lower_bound(a, sub, n, x):
    left = 0
    right = n
    pos = right

    while  left < right:
        mid = left + (right - left) // 2
        index = sub[mid]
        if a[index] >= x:
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
        if a[i] <= a[dp[0]]:
            dp[0] = i
        elif a[i] > a[dp[length-1]]:
            path[i] = dp[length-1]
            dp.append(i)
            length += 1
        else:
            pos = lower_bound(a,dp, length, a[i])
            path[i] = dp[pos-1]
            dp[pos] = i
    return length
array = []
cnt = 0
while True:
    n = int(input())
    if n == -1:
        cnt += 1
        print("Test #{}:".format(cnt))

        dp = [1] * len(array)
        for i in range(0, len(array)):
            for j in range(i):
                if array[j] >= array[i]:
                    dp[i] = max(dp[i],dp[j] + 1)

        print('  maximum possible interceptions: {}'.format(max(dp)))
        array = []
        n1 = int(input())
        if n1 == -1:
            break
        else:
            print("")
            array.append(n1)
    else:
        array.append(n)

