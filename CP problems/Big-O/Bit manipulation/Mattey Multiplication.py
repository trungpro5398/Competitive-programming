from sys import stdin

t = int(stdin.readline())
while t:
    t -= 1
    n, m = [int(x) for x in stdin.readline().split()]

    sav = []
    cnt = 0
    while m:
        if m % 2:
            sav.append(cnt)
        m //= 2
        cnt += 1

    sav.reverse()
    for i in range(0, len(sav)):
        if i < len(sav) - 1:
            print('({}<<{}) +'.format(n, sav[i]), end= " ")
        else:
            print('({}<<{})'.format(n, sav[i]))