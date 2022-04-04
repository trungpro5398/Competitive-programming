n = int(input())
a = [int(x) for x in input().split()]
cnt = sum(a)
for i in range(0,n):
    a[i] *= n
res = 0
cur = 0
mp = dict()
for i in range(0, n):
    cur += (a[i] - cnt)

    if (cur == 0):
        res+= 1
    if cur in mp:
            res += mp[cur]
    if cur in mp:
        mp[cur] += 1
    else:
        mp[cur] = 1
print(res)