import bisect
import math
from sys import stdin


def stoneGame():
    t = int(input())
    while( t ):
        t -= 1
        n = int(input())
        a = [0] * n
        min_num = 101
        max_num = 0
        min_pos = max_pos = 0
        a = input().rstrip().split()
        for i in range(0, n):
            aa = int(a[i])
            if aa < min_num:
                min_num = min(min_num, aa)
                min_pos = i
            if aa > max_num:
                max_num = max(max_num, aa)
                max_pos = i
        res = min(abs(max_pos - n) + min_pos + 1, max(min_pos, max_pos) + 1, abs(min_pos - n) + max_pos + 1,
                  max(abs(min_pos- n), abs(max_pos-n)) )
        print(res)
def f_and_c():
    t = int(input())
    while (t):
        t -= 1
        n = int(input())
        a = [0] * n
        a = input().rstrip().split()
        cnt_less = cnt_over = 0
        average = 0
        for i in a:
            average += int(i)
        if average % len(a) != 0:
            print(-1)
            continue
        average /= len(a)
        average = int(average)
        for i in a:
            ii = int(i)
            if ii > average:
                cnt_over += 1
        print(cnt_over)



def num_of_pairs():
    t = int(input())
    while (t):
        t -= 1
        b = input().rstrip().split()
        n, l1, r1 = int(b[0]), int(b[1]), int(b[2])
        a = input().rstrip().split()
        aa = []
        for i in a:
            aa.append(int(i))
        aa.sort()
        ans = 0
        for i in range(0, len(aa)):
            ans += bisect.bisect_right(aa, r1 - aa[i], lo=0, hi=len(aa))
            ans -= bisect.bisect_left(aa, l1 - aa[i], lo=0, hi=len(aa))
            if l1 <= 2 * aa[i] <= r1:
                ans -= 1
        print(ans // 2)
def sieve(n):
    primes = []
    isPrime = [True for i in range(n + 1)]
    isPrime[0] = isPrime[1] = False
    i = 2
    while i * i <= n:
        if isPrime[i] == True:
            for j in range(i ** 2, n + 1, i):
                isPrime[j] = True
        i += 1
    for a in range(2, n + 1):
        if isPrime[a] == True:
            primes.append(a)
        else:
            pass  # This is optional
    return primes
def factorize(x):
    primes = sieve(x)
    factors = []
    while x != 1:
        for i in primes:
            if x % i == 0:
                factors.append(i)
                x = x / i
                break
            else:
                pass # This is optional
    return factors

def div( x):
    i = 2
    cnt  = 0
    while i * i <= x:
        while x % i == 0:
            cnt += 1
            x /= i

        i += 1
    if x > 1:
        cnt += 1
    return cnt
def dividing_num():
    # input via readline method
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        # array input similar method
        c = [int(x) for x in stdin.readline().split()]
        a, b, k = int(c[0]), int(c[1]), int(c[2])

        if k == 1:
            if a != b and (b % a == 0 or a % b == 0):
                print("YES")
            else:
                print("NO")
        else:
            res_a = div(a)
            res_b = div(b)
            if res_a + res_b >= k:
                print("YES")
            else:
                print("NO")
def count(s):
    cnt = 0
    for i in range(0, len(s)):
        if s[i] == 'h' and s[i:i+4] == "haha":
            cnt += 1
    return cnt

def funny_substrings():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        n = stdin.readline()
        n = int(n)
        arr = [0] * 2000
        arr1 = [""] * 2000
        arr2 = [""] * 2000
        while (n):
            n -= 1
            c = [x for x in stdin.readline().split()]
            if c[1] == ":=":
                sav = hash(c[0]) % 1093
                arr[sav] = count(c[2])
                arr1[sav] = c[2][0:3]
                arr2[sav] = c[2][len(c[2]) - 3: len(c[2])]
                print(arr1[sav], arr2[sav])
            else:
                sav = hash(c[0]) % 1093
                sav1 = hash(c[2]) % 1093
                sav2 = hash(c[4]) % 1093
                arr[sav] = arr[sav1] + arr[sav2] + count(arr2[sav1] + arr1[sav2])
                #print(arr[sav], arr2[sav1], arr1[sav2], count(arr2[sav1] + arr1[sav2]))
                s = arr1[sav1] + arr2[sav1][len(arr2[sav1]) - len(arr1[sav1]): len(arr2[sav1])] + arr1[sav2] + arr2[sav2][len(arr2[sav2]) - len(arr1[sav2]): len(arr2[sav2])]
                arr1[sav] = s[0 : 3]
                arr2[sav] = s[len(s) - 3: len(s)]
                print(arr[sav], c[2], c[4],  arr1[sav], arr2[sav])
                if n == 0:
                    print(arr[sav])
def F():
    t = stdin.readline()
    t = int(t)

    while (t):
        t -= 1
        a = [int(x) for x in stdin.readline().split()]
        l, r = a[0], a[1]
        res = 0
        while l != 0 or r != 0:
            res += r - l
            r //= 10
            l //=10
        print(res)
F()