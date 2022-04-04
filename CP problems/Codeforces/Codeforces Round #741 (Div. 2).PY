import copy
import math
from sys import stdin


def A():
    t = int(stdin.readline())
    while t:
        t -= 1
        l, r = [int(x) for x in stdin.readline().split()]
        k = r // 2
        if k < l:
            print(r-l)
        else:
            print(r - k - 1)


def B():
    t = int(stdin.readline())
    def f1(s):
        for i in s:
            if i == '4' or i == '6' or i == '8' or i == '9':
                return 1, i
        return None
    def f2(s):
        for i in range(len(s)-1,-1,-1):
            if (ord(s[i])-ord('0')) % 2 == 0 or (ord(s[i])-ord('0')) % 3 == 0 or (ord(s[i])-ord('0')) % 5 == 0 or (ord(s[i])-ord('0')) % 7 == 0:
                    return i,s[0:i]
        return None
    while t:
        t -= 1
        k = int(stdin.readline())
        n = input()
        if f1(n):
            a = f1(n)
            print(a[0])
            print(int(a[1]))
            continue
        sum = 0
        for i in n:
            sum += ord(i) - ord('0')
        if sum % 3 == 0 or sum % 9 == 0:
            print(k)
            print(n)
            continue
        if f2(n):
            a = f2(n)

            print(a[0])
            print(int(a[1]))
            continue



def C():
    t = int(stdin.readline())
    while t:
        t -= 1
        a = [int(x) for x in stdin.readline().split()]




def D():
    t = int(stdin.readline())
    while t:
        t -= 1



def E():
    t = int(stdin.readline())
    while t:
        t -= 1

print(1111&101)
C()