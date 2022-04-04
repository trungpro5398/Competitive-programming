try:
    while True:
        s, s1= input().split()
        n = len(s)
        m = len(s1)
        s = '#' + s
        s1 = '#' + s1
        lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i] == s1[j]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        i = n
        j = m
        res = ""
        while i > 0 or j > 0 :
            if i == 0:
                res += s1[j]
                j -= 1
            elif j == 0:
                res += s[i]
                i -= 1
            else:
                if s[i] == s1[j]:
                    res += s[i]
                    i -= 1
                    j -= 1
                elif lcs[i][j] == lcs[i-1][j]:
                    res += s[i]
                    i -= 1
                else:
                    res += s1[j]
                    j -= 1

        print(res[::-1])


except:
    pass