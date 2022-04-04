import random
import sys


def isProbablyPrime(a, s, t ,n):
    x = pow(a, t, n)
    if x == 1:
        return True
    for i in range(0, s):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return False
def millerRabinRandomisedPrimality_(n,k = 7):
    if n <= 1 or n == 4:
        return False;
    if n <= 3:
        return True;

    s, t = 0, n - 1
    while t % 2 == 0:
        s += 1
        t //= 2
    for _ in range(k):
        a = random.randint(2, n - 2);
        if not isProbablyPrime(a,s,t,n):
            return False
    return True
if __name__ == '__main__':
    n = int(sys.argv[1])
    if n == 1:
        print(1)
    a = random.randint(pow(2,n-1), pow(2,n)-1)
    while not millerRabinRandomisedPrimality_(a):
        a = random.randint(pow(2, n - 1), pow(2, n) - 1)
    print(a)