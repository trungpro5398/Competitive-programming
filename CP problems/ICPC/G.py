
def work():
    s = input()
    cnt = [0] *256
    if s[0] == 'G':
        for i in range(1, len(s)):

            if s[i] > s[i-1] and s[i] in "AEIOU":
               continue
            if s[i] == 'L' or s[i] == 'G':
                continue
            else:

                return "no"
    else:
        return "no"
    return "yes"
print(work())