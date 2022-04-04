

dp = [0] * 22

for i in range(1, 22):
    dp[i] = i**3
cal = [0] * (10000+1)
cal[0] = 1
for i in range(1,22):
    for j in range(dp[i],10000+1):
        cal[j] += cal[j-dp[i]]
try:
    while True:
        n = int(input())


        print(cal[n])
except:
    pass