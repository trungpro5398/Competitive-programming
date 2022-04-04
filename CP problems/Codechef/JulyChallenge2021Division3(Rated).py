import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        A = [int(x) for x in stdin.readline().split()]
        d, x,y, z = A[0], A[1], A[2], A[3]
        print(max(7*x, y * d + z * (7-d)))

def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        A = [int(x) for x in stdin.readline().split()]
        g, c = A[0], A[1]
        print(c**2// (2*g))
def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        A = [int(x) for x in stdin.readline().split()]
        N, K = A[0], A[1]
        A = [int(x) for x in stdin.readline().split()]
        A.sort()
        for i in range(0, len(A)):
            print(i)



def remove_1element_maxgcd(a, n):
    # Prefix and Suffix arrays
    Prefix = [0 for i in range(n + 2)]
    Suffix = [0 for i in range(n + 2)]

    # Single state dynamic programming relation
    # for storing gcd of first i elements
    # from the left in Prefix[i]
    Prefix[1] = a[0]
    for i in range(2, n + 1):
        Prefix[i] = math.gcd(Prefix[i - 1], a[i - 1])

    # Initializing Suffix array
    Suffix[n] = a[n - 1]

    # Single state dynamic programming relation
    # for storing gcd of all the elements having
    # greater than or equal to i in Suffix[i]
    for i in range(n - 1, 0, -1):
        Suffix[i] = math.gcd(Suffix[i + 1], a[i - 1])


    # If first or last element of
    # the array has to be removed
    ans = max(Suffix[2], Prefix[n - 1])

    # If any other element is replaced
    for i in range(2, n):
        ans = max(ans, math.gcd(Prefix[i - 1], Suffix[i + 1]))

    # Return the maximized gcd
    return ans
def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        if len(a) == 1:
            print(1)
            continue

        ans = remove_1element_maxgcd(a, len(a))

        if ans == 1:
            print(sum(a) - max(a) + 1)
        else:
            res = 0
            for i in a:
                if i % ans:
                    res += 1
                else:
                    res += int(i / ans)
            res1 = 0
            for i in range(0, len(a) - 1):
                if a[i] % a[0]:
                    res1 = copy.deepcopy(res)
                else:
                    res1 += int(a[i] / a[0])
            res1 += 1
            print(min(res, res1))



D()