from sys import stdin



while True:

    try:
        line = input()
        if line == '':
            break
        n, m = line.split()
        n = int(n)
        m = int(m)
        a = [int(x) for x in stdin.readline().split()]
        l = 1
        r = 10 ** 12
        ans = 0


        def cal(m, c):
            cap = c
            cnt = 1

            for i in range(0, n):
                if a[i] > c:
                    return False
                if a[i] > cap:
                    if cnt == m:
                        return False
                    cap = c
                    cnt += 1
                cap -= a[i]

            return True


        while l <= r:
            mid = (l + r) // 2
            if cal(m, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        print(ans)

    except(EOFError):
        break