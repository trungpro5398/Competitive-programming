import collections
import copy
from sys import stdin

from numpy.lib import math


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        temp = 1
        for i in range(n):
            print(temp, end= " ")
            temp += 2
        print()
def B():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        temp = 0
        for i in a:
            temp += i
        if temp % 3 != 0:
            print(-1)
        else:
            temp = []
            for i in a:
                if i % 3 != 0:
                    temp.append( i % 3)
            cnt = 0
            l = 0
            r = len(temp) - 1
            temp.sort()

            while l < r:
                if temp[l] % 3 != 0:
                    if temp[r] % 3 != 0:
                        cnt += 1
                        temp[l] -= 1
                        temp[r] += 1
                    else:
                        r -= 1
                else:
                    l += 1
            print(cnt)


def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        n = int(stdin.readline())
        a = [int(x) for x in stdin.readline().split()]
        res = 0
        for i in range(3, n+1):
            for j in range(n-i+1):
                k = ((j+i-1) - j) // 2 + j
                temp = 0
                temp = max(temp, (a[j] - a[k-1]) * (a[k-1] - a[j + i - 1]))
                temp = max(temp,(a[j] - a[k]) * (a[k] - a[j+i-1]))
                temp = max(temp, (a[j] - a[k+1]) * (a[k+1] - a[j + i - 1]))
                res += temp
        print(res)

def D():
    t = int(stdin.readline())
    while t:
        t -= 1
        n, k = [int(x) for x in stdin.readline().split()]
        a = [int(x) for x in stdin.readline().split()]
        a.sort()
        res = []
        for i in range(0, k-1):
            res.append(a[i])
        r = n
        while r > k - 1:
            r -= 1
            res.append(a[r])
        cnt = 1
        temp = 0
        for i in range(n-1):
            if res[i+1] >= res[i]:
                cnt += 1
            else:
                cnt = 1
            temp = max(temp, cnt)
        if temp != k:
            print(-1)
            continue
        for i in res:
            print(i, end = " ")
        print()



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

D()