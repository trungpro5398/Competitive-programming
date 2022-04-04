from sys import stdin

def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        A, B, X = a[0], a[1], a[2]
        print(abs((A-B)// X))

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        A = stdin.readline()
        if A[0] != "1":
            print("1" + A)
        else:
            print(A[0] + "0" + A[1:len(A)])
def C():
    t = int(stdin.readline())


    while t:
        t -= 1
        S = stdin.readline()
        S = S.strip()

        if S[0:2] == "</" and S[-1] == ">" and len(S) > 3:
            b = True
            for i in range(2, len(S)-1):
                if S[i] == " ":
                    b = False
                    break
                if S[i].isupper():
                    b = False
                    break
                if S[i].isalnum():
                    continue
                b = False
                break
            if b:
                print("SUCCESS")
            else:
                print("Error")
        else:
            print("Error")
def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        N = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        even = []
        odd = []
        for i in a:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        res = []
        even.sort()
        odd.sort()
        odd.reverse()
        while len(even):
            res.append(even.pop(0))
        while len(odd):
            res.append(odd.pop(0))
        for i in res:
            print(i, end=" ")
        print()
def E():
    t = int(stdin.readline())
    def isPowerof2(x):
        return (x and not (x & x-1))
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        A, B = a[0], a[1]
        if  isPowerof2(B):
            print("Yes")
        else:
            print("No")
def F():

    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        N, M, K = a[0], a[1], a[2]
        mat = [[0 for x in range(M)] for x in range(N)]
        mat1 = [[0 for x in range(M)] for x in range(N)]
        dp = [[0 for x in range(M)] for x in range(N)]
        for i in range(0, N * M):
            a = [int(x) for x in stdin.readline().split()]
            if mat[a[0]-1][a[1]-1] == 0:
                if i % 2 == 0:
                    mat[a[0]-1][a[1]-1] = 1
                else:
                    mat[a[0]-1][a[1]-1] = 2
                mat1[a[0]-1][a[1]-1] = i
        for i in range(0, N):
            for j in range(0, M):
                if mat[i][j] == 1:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        if mat[i][j-1] != 1:
                            dp[i][j] = 1

                        else:
                            dp[i][j] = dp[i][j-1] + 2
                            mat1[i][j] = max(mat1[i][j], mat1[i][j-1])
                else:
                    if j == 0:
                        dp[i][j] = 2
                    else:
                        if mat[i][j-1] != 2:
                            dp[i][j] = 2
                        else:
                            dp[i][j] = dp[i][j-1] + 2
                            mat1[i][j] = max(mat1[i][j], mat1[i][j - 1])
        f_k = 1 + (K-1) * 2
        Alc = []
        Bob = []
        for i in range(0, N):
            for j in range(0, M):
                if dp[i][j] == f_k:
                    cnt = 1
                    res = mat1[i][j]
                    for k in range(i-1, 0, -1):
                        if dp[i][j] == dp[k][j]:
                           cnt += 1
                           res = max(res, mat1[k][j])
                        else:
                            break
                    for k in range(i+1, N):
                        if dp[i][j] == dp[k][j]:
                           cnt += 1
                           res = max(res, mat1[k][j])
                        else:
                            break
                    if cnt >= K:
                        Alc.append(res)
        f_k = 2 + (K - 1) * 2
        for i in range(0, N):
            for j in range(0, M):
                if dp[i][j] == f_k:
                    cnt = 1
                    res = mat1[i][j]
                    for k in range(i-1, 0, -1):
                        if dp[i][j] == dp[k][j]:
                           cnt += 1
                           res = max(res, mat1[k][j])
                        else:
                            break
                    for k in range(i+1, N):
                        if dp[i][j] == dp[k][j]:
                           cnt += 1
                           res = max(res, mat1[k][j])
                        else:
                            break
                    if cnt >= K:
                        Bob.append(res)
        Alc.sort()
        Bob.sort()
        if len(Alc) == 0 and len(Bob) == 0:
            print("Draw")
        elif len(Alc) == 0:
            print("Bob")
        elif len(Bob) == 0:
            print("Alice")
        else:
            if Alc[0] < Bob[0]:
                print("Alice")
            else:
                print("Bob")

def K():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        N, K = a[0], a[1]
        p = [int(x) for x in stdin.readline().split()]

F()