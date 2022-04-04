import copy

k = int(input())
n = input()
a = []

res = 0
for i in n:
    res += ord(i) - ord('0')
    a.append(ord(i) - ord('0'))
if res > k:
    print(0)
else:
    ans = 0

    a.sort()

    cnt = 0
    l = 0
    while res < k :
        res += 9 - a[l]
        l += 1

    print(l)