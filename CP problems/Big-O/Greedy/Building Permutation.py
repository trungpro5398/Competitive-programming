from sys import stdin

n = int(input())
a = [int(x) for x in stdin.readline().split()]
a.sort()
ans = 0
for i in range(1, n+1):
    ans += abs((i-a[i-1]))
print(ans)