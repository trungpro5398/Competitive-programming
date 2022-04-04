def A():
    times = [[3,10],[1,5],[2,6]]
    targetFriend = 0

    li = []
    maxx = 0
    for i in range(len(times)):
        maxx = max(maxx, times[i][1])

    li.sort()
    chair = 0
    dp = [0] * (maxx+10)
    dpch = [0] * (maxx + 10)
    dpch1 = [0] * (maxx + 10)
    for i in range(len(times)):
        dp[times[i][0]] = i + 1
        dp[times[i][1]] = -( i + 1)

    for i in range(1, maxx+1):

        if dp[i] == 0:
            continue

        if dp[i] == targetFriend + 1:
            while dpch1[chair] != 0:
                chair += 1

            return chair
        if dp[i] > 0:
            while dpch1[chair] != 0:
                chair += 1
            dpch[dp[i]] = chair
            dpch1[chair] = 1
            chair += 1
            while dpch1[chair] != 0:
                chair+= 1
        elif dp[i] < 0:

            chair = dpch[-dp[i]]
            dpch[-dp[i]] = 0

A()