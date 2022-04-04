import collections
import copy
from sys import stdin

from numpy.lib import math


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        a,b,p,q= [int(x) for x in stdin.readline().split()]
        if a == p and b == q:
            print(0)
        elif ( a + b ) % 2 !=  (p+q) % 2 :
            print(1)
        else:
            print(2)
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        b = [int(x) for x in stdin.readline().split()]
        a = [0] * n
        temp = 1
        res = True
        for i in range(n):
            if i > 0 and b[i] > b[i - 1]:
                res = False
                break
            if i > 0 and b[i-1] % b[i] != 0:
                res = False
                break
        if res:
            for i in range(n):
                print(b[i], end = " ")
            print()
        else:
            print(-1)

def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, m = [int(x) for x in stdin.readline().split()]
        s = [""] * n
        s2 = []
        for i in range(n):
            s[i] = input()
            s2.append((s[i].count('1'), s[i]))
        s2.sort()
        s1 = ""
        for i in s2:
            a,b = i
            s1 += b
        cnt0 = 0
        cnt = [0] * len(s1)
        for i in range(len(s1)):
            if i > 0:
                cnt[i] = cnt[i-1]
            if s1[i] == '0':
                cnt[i] += 1
                cnt0 += 1
        ans = 0
        for i in range(len(s1)):

            if s1[i] == '1' and i < len(s1) - 1:
               ans += cnt0 - cnt[i]
        print(ans)

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        s = input()
        cntA = s.count('0')
        cntB = s.count('1')
        cnt = 1
        while cntA != 0 and cntB != 0:
            if cntA == 1 or cntB == 1:
                cnt += 1
                break
            if cntA > cntB:
                cntA -= 1
            else:
                cntB -= 1
            cnt += 1
        if cnt % 2 == 0:
            print("Alice")
        else:
            print("Bob")

def E():
    MAX_SIZE = 10**5 + 10

    # isPrime[] : isPrime[i] is true if
    #             number is prime
    # prime[] : stores all prime number
    #           less than N
    # SPF[] that store smallest prime
    # factor of number [for ex : smallest
    # prime factor of '8' and '16'
    # is '2' so we put SPF[8] = 2 ,
    # SPF[16] = 2 ]
    isprime = [True] * MAX_SIZE
    prime = []
    SPF = [None] * (MAX_SIZE)

    # function generate all prime number
    # less then N in O(n)
    def manipulated_seive(N):

        # 0 and 1 are not prime
        isprime[0] = isprime[1] = False

        # Fill rest of the entries
        for i in range(2, N):

            # If isPrime[i] == True then i is
            # prime number
            if isprime[i] == True:
                # put i into prime[] vector
                prime.append(i)

                # A prime number is its own smallest
                # prime factor
                SPF[i] = i

            # Remove all multiples of i*prime[j]
            # which are not prime by making is
            # Prime[i * prime[j]] = false and put
            # smallest prime factor of i*Prime[j]
            # as prime[j] [ for exp :let i = 5 , j = 0 ,
            # prime[j] = 2 [ i*prime[j] = 10 ]
            # so smallest prime factor of '10' is '2'
            # that is prime[j] ] this loop run only one
            # time for number which are not prime
            j = 0
            while (j < len(prime) and
                   i * prime[j] < N and
                   prime[j] <= SPF[i]):
                isprime[i * prime[j]] = False

                # put smallest prime factor of i*prime[j]
                SPF[i * prime[j]] = prime[j]

                j += 1

    manipulated_seive(10**5+1)
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k = [int(x) for x in stdin.readline().split()]
        res = [1]
        k1 = copy.deepcopy(k)
        a = 1
        k -= 1
        res1 = False
        while k:
            if prime[a] > n:
                break
            if prime[a] <= n < prime[a] * 2:
                res.append(prime[a])
                k -= 1
            a += 1
            if n - len(res) == k1:
                print("Yes")
                temp = 0
                for i in range(n):
                    if i in res:
                        continue
                    print(i, end=" ")
                print()
                res1 = True
                break
        if res1:
            continue
        if k > 0:
            print("No")
        else:
            print("Yes")
            for i in res:
                print(i, end = " ")
            print()

E()