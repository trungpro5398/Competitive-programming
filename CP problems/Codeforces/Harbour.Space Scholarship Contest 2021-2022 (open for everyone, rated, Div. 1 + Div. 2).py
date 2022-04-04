import copy
from sys import stdin

def A():
    t = int(stdin.readline())

    while t:
        n = int(stdin.readline())
        t -= 1
        n += 1
        print(int(n // 10))
def B():
    t = int(stdin.readline())

    while t:

        t -= 1
        s = stdin.readline()
        s1 = stdin.readline()
        s2 = copy.deepcopy(s)
        s2 =s2[::-1]
        res = False
        for i in range(1, len(s1)):
            for j in range(0, len(s)-i):
                sav = len(s) - j - i
                sav1 = int(sav + 1)
                sav2 = int(sav1+len(s1) - i-1)
                sav3 = len(s1)-1
                # print(s[j:j + i], s1[0:i], s2[sav1:sav2], s1[i:sav3], sav, sav1, sav2)
                if s[j:j+i] == s1[0:i] and s2[sav1:sav2] == s1[i:sav3]:

                    res = True
                    break
        if res:
            print("YES")
        else:
            print("NO")



def C():
    t = int(stdin.readline())

    while t:

        t -= 1
        s = stdin.readline()
        s1 = copy.deepcopy(s)
        s = list(s)
        s1 = list(s1)
        for i in range(0, len(s)):
            if i % 2 == 0 and s[i] == '?':
                s[i] = "1"
                s1[i] = '0'
            elif i % 2 == 1 and s1[i] == '?':
                s1[i] = "1"
                s[i] = "0"
        res = 10
        cnt = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        print(s)
        print(s1)
        for i in range(len(s)):
            if s[i] == '1':
                if i % 2 == 0:
                    cnt += 1
                else:
                    cnt1 += 1
            if s[i] == '0':
                if i % 2 == 0:
                    cnt2 += 1
                else:
                    cnt3 += 1

            if cnt + cnt2 >= 5 or cnt1 + cnt3 >= 5and max(cnt,cnt1) > min(cnt1, cnt):
                print(cnt + cnt2, i)
                res = min(res,i + 1)
                break

        cnt = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for i in range(len(s)):
            if s1[i] == '1':
                if i % 2 == 0:
                    cnt += 1
                else:
                    cnt1 += 1
            if s1[i] == '0':
                if i % 2 == 0:
                    cnt2 += 1
                else:
                    cnt3 += 1
            print(cnt + cnt2, i)
            if cnt + cnt2 >= 5 or  cnt1 + cnt3 >= 5 and max(cnt, cnt1) > min(cnt1, cnt):
                print(cnt + cnt2, i)
                res = min(res, i + 1)
                break
        print(res)
C()