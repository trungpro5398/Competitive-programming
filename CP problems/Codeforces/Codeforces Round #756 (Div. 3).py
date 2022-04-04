from sys import stdin


def A():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        if n % 2 == 0:
            print(0)
        else:
            a = []
            while n:
                a.append(n % 10)
                n //= 10
            if a[-1] % 2 == 0:
                print(1)
            else:
                res = False
                for i in a:
                    if i % 2 == 0:
                        res = True
                        break
                if res: print(2)
                else:
                    print(-1)

def B():
    t = int(input())
    while t:
        t -= 1
        a, b = [int(x) for x in stdin.readline().split()]
        a1 = min(a,b)
        b1 = max(a,b)
        

def C():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        x = [int(x) for x in stdin.readline().split()]
        maxX = max(x)
        if x[0] != maxX and x[-1] != maxX:
            print(-1)
            continue
        if n == 1:
            print(1)
            continue
        if x[-1] == maxX:
            a = x[0:n - 1]
            a.reverse()
            a.append(x[-1])
            for i in a:
                print(i, end=" ")
        else:
            a = x[1:n]
            a.reverse()
            a.insert(0, x[0])
            for i in a:
                print(i, end=" ")
        print()

def D():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        x = [int(x) for x in stdin.readline().split()]
        s = input()
        l, r = [], []
        for i in range(0, n):
            if s[i] == 'B':
                l.append(x[i])
            else:
                r.append(x[i])
        l.sort()
        r.sort()
        r.reverse()
        ans = True
        for i in range(0, len(l)):
            if l[i] < i + 1:
                ans = False
        for i in range(0, len(r)):
            if r[i] > n - i:
                ans = False
        if ans:
            print("yes")
        else:
            print("no")
B()