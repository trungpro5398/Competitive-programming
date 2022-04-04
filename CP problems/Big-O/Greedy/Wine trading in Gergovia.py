from sys import stdin

while True:
    n = int(input())
    if n == 0:
        break
    t = [int(x) for x in stdin.readline().split()]
    ans = 0
    cnt = t[0]
    for i in range(1, n):
        ans += abs(cnt)
        cnt += t[i]
    print(abs(ans))