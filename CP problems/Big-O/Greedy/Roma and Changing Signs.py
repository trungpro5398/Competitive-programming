from sys import stdin

n, k = map(int, input().split())
a = [int(x) for x in stdin.readline().split()]
a.sort()
ans = 0
for i in range(0, len(a)):
    if a[i] < 0 and k > 0:
        a[i] = abs(a[i])
        ans += a[i]
        k -= 1
    else:
        ans += a[i]
        if k >= 2:
            k -= 2
if k > 0:
    a.sort()
    if k % 2 == 1:
        ans -= a[0] * 2

print(ans)