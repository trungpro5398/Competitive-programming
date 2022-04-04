t = int(input())
while t:
    t -= 1
    d = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    s = ''
    n = input()
    cnt = 0
    l = 0
    for i in n:
        s += d[i]
        cnt += int(i)
        l += 1
    i = 0
    if cnt < l:
        a = s[:cnt]
        if a == a[::-1]:
            print('YES')
        else:
            print('NO')
    else:
        while l < cnt:
            s += s[i]
            i += 1
            l += 1
            if i == l:
                i = 0

        if s == s[::-1]:
            print('YES')
        else:
            print('NO')
