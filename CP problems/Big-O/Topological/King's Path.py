from sys import stdin

a = [int(x) for x in stdin.readline().split()]

x, y , x1, y1 = a[0], a[1], a[2], a[3]

n = int(input())

s = {}
for i in range(n):
    c = [int(x) for x in stdin.readline().split()]
    r, a, b = c[0], c[1], c[2]
    for i in range(a, b+1):
        s[(r,i)] = -1

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
s[(x,y)] = 1
queue = [(x,y)]

while queue:
    sav = queue.pop(0)
    for i in range(8):
        sav1 = (dx[i] + sav[0], dy[i] + sav[1])
        if sav1 in s and s[sav1] == -1:
            queue.append(sav1)
            s[sav1] = s[sav] + 1
print(max(-1, s[(x1,y1)]-1))