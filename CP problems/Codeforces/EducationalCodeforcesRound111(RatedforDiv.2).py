from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        s = int(stdin.readline())
        cnt = []
        res = 1
        cnt.append(1)
        while s > res:
            s -= res
            res += 2
            if s < res:
                cnt.append(s)
            else:
                cnt.append(res)

        print(len(cnt))

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        s1 = [int(x) for x in stdin.readline().split()]
        n, a, b = s1[0], s1[1], s1[2]
        s = stdin.readline()
        cnt = 0
        res = 0
        for i in range(0, len(s)):
            if i == len(s) - 1:
                if s[i] == '0':
                    res += a * (cnt+1) + b
                break
            if s[i] == s[i + 1] == '0':
                cnt += 1
            else:
                if s[i] == '0':
                    res += a * (cnt+1) + b
                cnt = 0

        cnt_1 = 0
        for i in s:
            if i == '1':
                cnt_1 += 1
        if cnt_1 >0:
            res += a * cnt_1 + b


        res1 = 0
        cnt = 0
        for i in range(0, len(s)):
            if i == len(s) - 1:
                if s[i] == '1':
                    res1 += a * (cnt+1) + b
                break
            if s[i] == s[i + 1] == '1':
                cnt += 1
            else:
                if s[i] == '1':
                    res1 += a * (cnt+1) + b
                cnt = 0

        cnt_1 = 0
        for i in s:
            if i == '0':
                cnt_1 += 1
        if cnt_1 > 0:
            res1 += a * cnt_1 + b
        print(max(res, n * (a + b), res1))

def count(a):
    n = len(a)
    for j in range(0, n):
        for k in range(j + 1, n):
            for k1 in range(k + 1, n):
                if min(a[j], a[k1]) <= a[k] <= max(a[j], a[k1]):
                    return False
    return True
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = 0
        for i in range(1, 5):
            for j in range(0, n - i + 1):
                res += count(a[j:j+i])
        print(res)

C()