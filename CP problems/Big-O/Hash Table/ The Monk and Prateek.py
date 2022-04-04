import copy
from sys import stdin

n = int(input())
a =[int(x) for x in stdin.readline().split()]
def f(N):
    b = copy.deepcopy(N)
    ans = 0
    while b:
        ans += b % 10
        b //= 10
    return N ^ ans

p = []

for i in a:
    p.append(f(i))

p.sort()
cnt = [0] * n
m = 0
cnt[0] = 1
ans = 1
mx = 1
print(p)
for i in range(1, n):
    if p[i] == p[i-1]:
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = 1
        ans += cnt[i-1] - 1
    mx = max(mx, cnt[i])
    if mx > 1:
        m = 1
ans += cnt[n-1] - 1
if m == 0:
    print("{} {}".format(p[n-1], 0))
else:
    for i in range(n):
        if cnt[i] == mx:
            print("{} {}".format(p[i], ans-1))
            break

