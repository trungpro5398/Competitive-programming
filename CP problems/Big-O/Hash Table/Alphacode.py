

while True:
    s = input()
    if s == '0':
        break
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        if s[i]!= '0':
            dp[i] = dp[i-1]
        if 10<=int(s[i-1] + s[i]) <= 26:
            dp[i] += dp[max(0,i-2)]

    print(dp[len(s)- 1])
