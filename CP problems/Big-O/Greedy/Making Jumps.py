

dx = [2,-2,2,-2,1,-1,1,-1]
dy = [1,1,-1,-1,2,2,-2,-2]
t = 1
while True:
    n = input()
    n = n.split()
    if int(n[0]) == 0:
        break
    dp = [ [0 for _ in range(10)] for _ in range(10)]
    sum = 0
    l = 0
    st = 0
    for i in range(1, len(n), 2):
        x = int(n[i])
        y = int(n[i+1])
        sum += y
        if l == 0:
            st = x
        for j in range(0, y):
            dp[l][j+x] = 1
        l += 1
    ans = 0
    dp[0][st] = 2

    def dfs(cur, cnt):
        global ans
        ans = max(ans, cnt)
        # print(cur, cnt)
        for i in range(0, 8):
            x = dx[i] + cur[0]
            y = dy[i] + cur[1]
            sav = (x,y)
            if 0 <= x < 10 and 0<= y < 10 and dp[x][y] == 1:
                dp[x][y] = 2
                dfs((x,y), cnt + 1)
                dp[x][y] = 1
    dfs((0, st), 1)
    if sum - ans == 1:
        print('Case {a}, {b} square can not be reached.'.format(a=t, b=sum-ans))
    else:
        print('Case {a}, {b} squares can not be reached.'.format(a=t, b=sum - ans))
    t += 1
