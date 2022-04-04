t = int(input())
for i in range(t):
    n, b = map(int, input().split())
    res = 0
    for j in range(b):
        a = list(map(int, input().split(' ')))
        cnt = 1
        for k in range(1, len(a), 1):
            cnt = (cnt * a[k]) % n
        res = (res + cnt) % n
    print(res)





