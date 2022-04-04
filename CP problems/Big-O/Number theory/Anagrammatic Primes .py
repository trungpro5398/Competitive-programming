
anagramic = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 199, 311, 337, 373, 733, 919, 991]
while True:
    n = int(input())
    if n == 0:
        break
    r = len(anagramic) - 1

    if n > anagramic[r]:
        print(0)
    else:
        if n <= 1:
            print(2)
            continue
        while n < anagramic[r]:
            r -= 1
        k = 1
        while n:
            k *= 10
            n //=10
        if anagramic[r+1] < k:
            print(anagramic[r+1])
        else:
            print(0)
