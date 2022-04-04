from sys import stdin


def A():
    t = stdin.readline()
    t = int(t)

    while (t):
        t-= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        b = [0] * len(a)
        l = 0

        for i in range(0, len(a) // 2):
            b[l] = a[i]
            l += 2
        l = 1
        for i in range(len(a)//2 , len(a)):
            b[l] = a[i]
            l += 2
        for i in b:
            print(i, end=" ")
        print()

def B():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        n = int(stdin.readline())
        if n % 11 == 0:
            print("YES")
        else:
            a = n % 11
            if  n - a * 111 >= 0:
                print("YES")
            else:
                print("NO")
def C():
    t = stdin.readline()
    t = int(t)

    a = [int(x) for x in stdin.readline().split()]
    arr = [[0 for _ in range(2001)] for _ in range(2001)]
    arr1 = [[0 for _ in range(2001)] for _ in range(2001)]
    res = 0
    res_posi = 0
    for i in range(0, len(a)):
        arr[0][i] = a[i]
    for i in range(1, len(a)):
        for j in range(0, len(a)):
            if arr[i-1][j-1] + a[j] >= 0:
                arr1[i][j] = arr1[i][j-1] + 1
                arr[i][j] = arr[i-1][j-1] + a[j]
            
    print(a)
    print(res)


C()