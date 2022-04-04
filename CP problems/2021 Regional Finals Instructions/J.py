
n = int(input())

a = list(map(int, input().split()))
cnt = 1
cnt1 = a[0]
for i in range(1, len(a)):
    cnt ^= i +1
    cnt1 ^= a[i]
print(cnt ^ cnt1)