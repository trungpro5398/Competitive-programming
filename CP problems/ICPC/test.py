from sys import stdin

n = int(input())

a = [int(x) for x in stdin.readline().split()]
a.sort()
b = [int(x) for x in stdin.readline().split()]
b.sort()

if a == b:
    print("marvelous")
else:
    print("error")