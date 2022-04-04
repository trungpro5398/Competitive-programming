
t = int(input())

for k in range(1, t+1):
    s = input()
    dp = [0] * 258
    for i in s:
        dp[ord(i)] += 1
    lo = []
    
    for i in range(0,258):
        if dp[i] != 0:
            lo.append([dp[i], i])
    lo.sort()
    b = True
    print("Case #{}: ".format(k), end="")
    s1= ""
    for i in s:
        r = len(lo) - 1
        if len(lo) > 0:
            while ord(i) == lo[r][1]:
                r -= 1
                if r < 0:
                    break

        s1 += chr(lo[r][1])
        lo[r][0] -= 1
        if lo[r][0] == 0:
            lo.remove([lo[r][0], lo[r][1]])
        if len(lo) == 0:
            break
    for i in range(0, len(s)):
        if s[i] == s1[i]:
            b = False
            break
    if not b or len(s) != len(s1):
        print("IMPOSSIBLE")
    else:
        for i in s1:
            print(i, end="")
        print()