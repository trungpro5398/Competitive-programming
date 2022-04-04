def get(x, y, h, w):
    res = 0
    for i in range(x, x + h):
        for j in range(y, y + w):
            if a[i][j] == '1':
                res += 1
    return res

def BtoD(x, y, h, w):
    if h == 0 or w == 0:
        return ""

    cnt = get(x, y, h, w)

    if cnt == 0:
        return '0'
    elif cnt == h * w:
        return '1'

    s1 = BtoD(x, y, (h + 1) // 2, (w + 1) // 2)
    s2 = BtoD(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
    s3 = BtoD(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
    s4 = BtoD(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)

    return 'D' + s1 + s2 + s3 + s4

def DtoB(x, y, h, w):
    global cnt
    if h == 0 or  w == 0:
        return

    k = str[cnt]
    cnt += 1
    if k == '0':
        for i in range(x, x + h):
            for j in range(y, y + w):
                dest[i][j] = '0'
        return
    elif k == '1':
        for i in range(x, x + h):
            for j in range(y, y + w):
                dest[i][j] = '1'
        return
    DtoB(x, y, (h + 1) // 2, (w + 1) // 2)
    DtoB(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
    DtoB(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
    DtoB(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)
line = input()
while True:
    if line == '#':
        break
    line = line.split()
    h = int(line[1])
    w = int(line[2])
    x = line[0]
    iterator = 0
    str = ""
    while True:
        line = input()
        if line == "#" or ' ' in line:
            break
        str += line

    if x == 'B':
        a = [ str[i : i + w] for i in range(0, h * w, w)]
        print('D', end='')
        res = BtoD(0, 0, h, w)
    else:
        print('B', end='')
        dest = [ ['0' for i in range(w)] for j in range(h)]
        cnt = 0
        DtoB(0, 0, h, w)

        res = ''.join([''.join(line) for line in dest])
    print("%4d %3d" % (h, w))
    l = len(res)
    for i in range(l):
        print(res[i], end='')
        if (i + 1) % 50 == 0 or i == l - 1:
            print()