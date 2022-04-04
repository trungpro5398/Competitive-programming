
def find(s):
    if s[0] == 'm':
        for j in range(1, len(s)):
            if s[j] == 'e':
                if s[j+1] == 'o':
                    for k1 in range(j + 2, len(s)):
                        if s[k1] == 'w' and k1 == len(s) - 1:
                            return "meow"
            else:
                break

    if s[0] == 'r':
        for i in range(1, len(s)):
            if s[i] == 'o':
                if i > len(s) - 2:
                    break
                if s[i+1] == 'a' and s[i+2] =='r' and i + 2 == len(s) - 1:
                    return "roar"
            else:
                break
    if s[0] == 'p' and s[1] =='u':
        for j in range(2, len(s)):
            if s[j] == 'r':
                for k in range(j + 1, len(s)):
                    if s[k] == 'r' and k == len(s) - 1:
                        return "purr"
            else:
                break

    return "human noises"

t = int(input())
while t:
    t -= 1
    s = input()
    print(find(s))
