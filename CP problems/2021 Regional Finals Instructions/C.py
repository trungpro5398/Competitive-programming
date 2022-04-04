n,r, c =  list(map(int, input().split()))

mpX = dict()
mpY = dict()
ans = 0
for i in range(n):
    x, y =  list(map(int, input().split()))
    if x in mpX and y in mpY:
        continue
    if x in mpX:
        ans += r
        c -= 1
        mpY[y] = 1
        continue
    else:
        mpX[x] = 1
    if y in mpY:
        ans += c
        r -= 1
        mpX[x] = 1
        continue
    else:
        mpY[y] = 1
    ans += r + c - 1
    r -= 1
    c -= 1

print(ans)