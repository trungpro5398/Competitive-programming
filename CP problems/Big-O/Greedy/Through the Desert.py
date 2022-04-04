
while True:
    s = input()
    if s == "0 Fuel consumption 0":
        break
    s = s.split()
    ans = 0.0
    last = 0
    cons = float(s[3])
    leak = 0
    current = 0.0
    while True:
        s = input().split()
        current += cons * (float(s[0]) - last)/100
        current += leak * (float(s[0]) - last)
        ans = max(ans, current)
        last = float(s[0])
        if "Fuel" in s:
            cons = float(s[3])
        elif "Leak" in s:
            leak += 1
        elif "Gas" in s:
            current = 0
        elif "Mechanic" in s:
            leak = 0
        else:
            break
    print(format(ans, '.3f'))
