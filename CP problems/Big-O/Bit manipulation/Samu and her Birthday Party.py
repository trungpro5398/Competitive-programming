from sys import stdin
# Check if bitwise AND of any subset is power of two
t = int(stdin.readline())


while t:
    t -= 1
    n, k = [int(x) for x in stdin.readline().split()]
    d = [0] * n
    for i in range(n):
        s = input()
        sav = 0
        cnt = 1

        for j in range(k - 1, -1, -1):
            if s[j] == '1':
                sav += cnt
            cnt <<= 1

        d[i] = sav
    res = 10 ** 9
    def count_bit(bit):
        cnt  = 0
        while bit:
            cnt += bit & 1
            bit >>= 1
        return cnt
    # tất cả các trường hợp 1 có thể xuất hiện trong k bit
    for i in range(0, 1 << k):
        b = True
        for j in d:
            if j & i == 0:
                b = False
                break
        if b:
            res = min(res, count_bit(i))
    print(res)
