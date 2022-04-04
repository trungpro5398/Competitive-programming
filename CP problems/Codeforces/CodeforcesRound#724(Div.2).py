from sys import stdin


def A():
    t = stdin.readline()
    t = int(t)

    while (t):
        t-= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        arr = [0] * 101
        a.sort()
        i = 0
        while i < len(a) - 1:
            for j in range(i+1,len(a)):
                if abs(a[i] - a[j]) not in a:
                    a.append(abs(a[i] - a[j]))
                    i = -1
                    if len(a) > 300:
                        break
                if len(a) > 300:
                    break
            if len(a) > 300:
                break
            i += 1
            a.sort()
        if len(a) > 300:
            print("NO")
        else:
            print("YES")
            print(len(a))
            for i in a:
                print(i, end=" ")
            print()
def B():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        n = int(stdin.readline())
        a = stdin.readline()
B()