from sys import stdin




while True:
    try:
        a = [int(x) for x in stdin.readline().split()]
        if a[0] == 0:
            break
        dp = [0] * (a[0]+1)
        k = a[0]
        def backtracking(dp,pos, cnt):

            if cnt > 7:
                return
            if cnt == 7:

                for i in range(1, k+1):
                    if dp[i]:
                        print(a[i], end=" ")
                print()
                return
            for i in range(pos, k+1):
                if dp[i] == 0:
                    dp[i] = 1
                    backtracking(dp, i + 1, cnt+1)
                    dp[i] = 0
            return
        backtracking(dp, 1 , 1)
        print()

    except(EOFError):
        break