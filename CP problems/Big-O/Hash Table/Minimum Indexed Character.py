
t = int(input())

while t:
    t -= 1
    s = input()
    p = input()
    dp = [-1] * 26
    def convert(a):
        return ord(a) - ord('a')
    for i in range(0, len(s)):
        if dp[convert(s[i])] == -1:
            dp[convert(s[i])] = i

    cnt = 10**9
    for i in p:
        if dp[convert(i)] < cnt and dp[convert(i)] != -1:
            cnt = dp[convert(i)]
    if cnt == 10 ** 9:
        print("No character present")
    else:
        print(s[cnt])