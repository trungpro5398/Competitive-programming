
try:
    while True:
        s = []
        while True:
            s1 = input()
            if '#' in s1:
                break
            s1 = s1.split()
            for i in s1:
                s.append(i)
        s1 = []
        while True:
            s2 = input()
            if '#' in s2:
                break
            s2 = s2.split()
            for i in s2:
                s1.append(i)
        dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(len(s1)):
                if s[i] == s1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        n = len(s)
        m = len(s1)


        def printLCS(s, s1, n, m):
            lengthLCS = dp[-1][-1]
            res = [""] * lengthLCS
            i = n
            j = m

            while i >= 0 and j >= 0:
                if s[i - 1] == s1[j - 1]:
                    res[lengthLCS - 1] = s[i - 1]
                    i -= 1
                    j -= 1
                    lengthLCS -= 1
                elif dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

            for i in res:
                print(i, end=" ")


        printLCS(s, s1, n, m)

except:
    pass