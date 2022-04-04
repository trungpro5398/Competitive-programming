# from sys import stdin
#
# t = int(input())
# input()
#
# while t:
#     t -= 1
#     n, h = [int(x) for x in stdin.readline().split()]
#     def count(x):
#         cnt  = 0
#         while x:
#             cnt += x & 1
#             x >>= 1
#         return cnt
#     res = []
#     for i in range(1, 2 ** n):
#         if count(i) == h:
#             res.append(i)
#     for i in res:
#         cnt = 0
#         res1 = []
#         while i or cnt < n:
#             cnt += 1
#             res1.append(i & 1)
#             i >>= 1
#         res1.reverse()
#         for i in res1:
#             print(i, end="")
#         print()
#
def check(n, h, idx, start, res):
    if idx == h:
        print(''.join(res))
        return
    for i in range(n - h + idx, start - 1, -1):
        res[i] = '1'
        check(n, h, idx + 1, i + 1, res)
        res[i] = '0'
def solve():
    input()
    n, h = map(int, input().split())
    res = ['0'] * n
    check(n, h, 0, 0, res)

t = int(input())
for tc in range(t):
    solve()
    if tc < t - 1:
        print()