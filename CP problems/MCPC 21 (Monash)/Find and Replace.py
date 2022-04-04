s = input()
s1 = input()

while True:
    k = False
    for i in range(0, len(s1)):
        if i > len(s1) - 9:
            break
        if s1[i] == 'p':
            if s1[i:i+9] == "professor":
                s1 = s1[0:i] + s + s1[i+9:len(s1)]
                k = True

    if not k:
        break
print(len(s1))