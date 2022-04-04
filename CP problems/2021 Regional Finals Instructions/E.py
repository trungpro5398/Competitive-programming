
n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append((x,y))

a.sort()
cnt = 0

for i in range(1,n-1):
    x, y = a[i]
    xl,yl = a[i-1]
    xr, yr = a[i+1]
    if x <= yl and y >= xr:
        continue
    cnt += 1

x,y = a[0]
x1,y1 = a[1]
if x1 <= y:
    cnt += 1
x,y = a[-1]
x1,y1 = a[-2]
if x <= y1:
    cnt += 1
print(cnt)
