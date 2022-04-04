
t = int(input())

while t:
    t -= 1
    s = input().split(" ")
    s1 = input().split(" ")
    dp = [0] * 1000
    dp1 = [0] * 1000
    dp2 = [0] * 1000
    dp3 = [0] * 1000
    s2 = "SHCD"
    s3 = "23456789TJQKA"
    for i in s:
        dp[i[0]] += 1
        dp1[i[1]] += 1
    for i in s1:
        dp2[i[0]] += 1
        dp3[i[1]] += 1
    dp.sort()
    dp.reverse()
    dp1.sort()
    dp1.reverse()
    dp2.sort()
    dp2.reverse()
    dp3.sort()
    dp3.reverse()
