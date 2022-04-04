from sys import stdin

n, c = [int(x) for x in stdin.readline().split()]
print(min(n,c,(n+c) // 3))