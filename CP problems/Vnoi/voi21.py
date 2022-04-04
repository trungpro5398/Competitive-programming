from sys import stdin


def A():
    a = [int(x) for x in stdin.readline().split()]
    n, d1 = a[0], a[1]
    c = [int(x) for x in stdin.readline().split()]
    d = [0] * ( len(c) + 1)
    f = []
    for i in range(0, len(c)):
        d[c[i]] = i
    for i in range(0, len(c)):
        for j in range(1, d1+1):
            if c[i] + j < (len(c) + 1):
                if d[c[i] + j] > i:
                    f.append((i, d[c[i] + j]))
            if d[abs(c[i] - j)] > i:
                if d[abs(c[i] - j)] not in f:
                    f.append((i, d[abs(c[i] - j)]))
    f.sort()

    res = [0] * (len(f) + 1)
    sav = [0] * (len(f) + 1)
    for i in range(0, len(f)-1):
        for j in range(i+1, len(f)):
            if f[i][0] < f[j][0] and f[i][1] < f[j][1] and f[i][1] > f[j][0] :
                if res[i] > 0 and f[j][0] >= sav[i]:
                    continue
                res[j] = max(res[i] + 1, res[j])
                sav[j] = sav[i]
                if res[i] == 0:
                    sav[j] = max(f[i][1], sav[j])

    print(max(res) + 1)



A()