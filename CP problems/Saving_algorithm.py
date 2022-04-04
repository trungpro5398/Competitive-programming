from sys import stdin

n, c = [int(x) for x in stdin.readline().split()]

a = min(n,c)
b = max(n, c)
c = b // 2
d = b - c
if( a- c ) < 0:
    print(a)
elif a - c == 1:
    print(a)
else:
    if(d== 1):
        print(c + 1)
    else:
        print(c)