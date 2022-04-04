
while True:
    try:
        n = int(input())
    except EOFError:
        break
    x = 1 % n
    ans = 1
    while x != 0:
        x = (x * 10 + 1) % n
        ans += 1
    print(ans)