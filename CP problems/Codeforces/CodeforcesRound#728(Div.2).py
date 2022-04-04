from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        if n % 2 == 0:
            for i in range(1, n , 2):
                print(i+1, end=" ")
                print(i, end= " ")
            print()
        else:
            if n == 3:
                print("3 1 2")
                continue
            a = []
            for i in range(1,n+1):
                a.append(i)
            for i in range(0, n  - 1, 2):
                a[i], a[i+1] = a[i+1], a[i]
            if a[n-1] == n:
                a[n-1], a[n-2] = a[n-2], a[n-1]
            for i in a:
                print(i, end = " ")
            print()
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        cnt = 0
        b = []
        for i in range(0, len(a)):
            b.append((a[i], i + 1))
        b.sort()
        for i in range(0, len(b) - 1):
            for j in range(i+1, len(b)):
                if b[i][0] * b[j][0] > n * 2:
                    break
                if b[i][1] + b[j][1] == b[i][0] * b[j][0]:
                    cnt += 1
        print(cnt)
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        sum = 0
        ans = a[n-1]
        for i in range(0, n):
            ans -= (a[i]  * i - sum)
            sum += a[i]
        print(ans)
C()