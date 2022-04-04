from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        c, d =  [int(x) for x in stdin.readline().split()]
        if abs(c-d) % 2== 1:
            print(-1)
        elif c== 0 and d == 0:
            print(0)
        elif c == d:
            print(1)
        else:
            print(2)

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a =  [int(x) for x in stdin.readline().split()]
        even = 0
        odd = 0
        lo_e = []
        lo_o = []
        for i in range(0, n):
            if a[i] % 2 == 0:
                even+= 1
                lo_e.append(i+1)
            else:
                odd += 1
                lo_o.append(i+1)
        if n == 1:
            print(0)
            continue
        if abs(even-odd) >= 2:
            print(-1)
        else:
            res = 0
            res1 = 0
            res2 = 0
            res3 = 0
            l = 2
            l1 = 1
            for i in range(0, min(len(lo_e), len(lo_o))):
                res += lo_e[i] - l
                res1 += lo_o[i] - l
                res2 += lo_e[i] - l1
                res3 += lo_o[i] - l1
                l += 2
                l1 += 2


            print(min(max(res,res1), max(res2, res3)))

B()