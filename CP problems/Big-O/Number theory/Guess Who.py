from sys import stdin

n, f = [int(x) for x in stdin.readline().split()]

arr = [["" for i in range(f)] for j in range(n)]
fet = []
for i in range(f):
    x = input()
    fet.append(x)
for i in range(n):
    x = input().split(" ")
    for j in range(len(x)):
        arr[i][j] = x[j]

sav = []
sav1 = {}
res = []
q = 20
for i in range(n):
    for j in range(f):
        if j in res:
            continue
        if i not in sav1:
            print("QUERY {} = {}".format(fet[j], arr[i][j]))
            x = input()
            if x == "NO":
                sav1[i] = 1
                for k in range(i+1,n):
                    if arr[i][j] == arr[k][j]:
                        sav1[k] = 1
                break
                res.append((j, arr[i][j]))
            else:
                continue
            q -= 1
        if q == 0:
            break
    if q == 0:
        break


for i in range(n):
    if i not in sav1:
        c = True
        for j in range(f):
            if (j,arr[i][j]) in res:
                c = False
                break
        if c:
            print("GUESS {}".format(i + 1))
            break