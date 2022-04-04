import sys


if __name__ == '__main__':
    a = int(sys.argv[1])
    n = int(sys.argv[2])

    # generate all possible strings of length N from the alphabet A
    # each index we have A ways to choose so with N length we have A * A ... * A = A ^ N
    total = a ** n

    # exactly 1 distinct cyclic rotation, all characters in the string are the same
    # depend on how many alphabet size, we will get the the number of them
    # for example if A = 2 ( 'a', 'b' ) and N = 3, so we just have aaa and bbb to get exactly 1 distinct
    oneDistinct = a
    # The number of strings of length N from alphabet A with ≥ 2 distinct cyclic
    # rotations. When we subtract the case 1 distinct to the total case. We will get the case that ≥ 2 distinct cyclic
    # rotation
    twoOrMoreDistinct = total - a
    nDistinct = 0
    # if n == 1, n distinct also be 1 distinct
    # if we want to get 2 distinct the string should be like XYXYXY. So every two rotation the string will return the
    # initial string. If the string XYXYX. It is impossible to get the initial string.
    # My observation realized that x distinct ( x < n length) should be divisible by n.
    # The number of way to get all x distinct will be a ^ x ( x is the alphabet size)
    # Prove: for every x rotation the string will return the initial string. So if the first character we have a ways to
    # choose, then each character that are far from the first character x index can only have one choice because
    # if you choose other character which will return the different string, same for the second index,... the (x-1)th
    # index. That why all prime numbers just get n distinct numbers.
    if n == 1:
        nDistinct = oneDistinct
    elif n == 2 or n == 3 or n == 5 or n == 7:
        nDistinct = twoOrMoreDistinct
    else:
        # in this case n = 4, we just have 2 is divisible by 4
        if n == 4:
            nDistinct = total - a ** 2
        # in this case n =6, we have 2 and 3 are divisible by 6. However when we subtract the case 3 distinct
        # we also get the case aaa.., bbb..., ccc...,.. Then in the case 2 distinct, we also get the case aaa..., bbb...
        # ,ccc...,.. It will be duplicated so we must plus the case 1 distinct, which will have A ways.
        elif n == 6:
            nDistinct = total - a ** 3 - a ** 2 + a
        # in this case n = 8, we have 2, 4 are divisible by 4. While calculating case 4 distinct included all cases 2
        # distinct. Therefore, I only subtract for the case of 4 distinct.
        elif n == 8:
            nDistinct = total - a ** 4
        # in this case n = 9, we have only 3 is divisible by 9
        elif n == 9:
            nDistinct = total - a ** 3
        # in this case n = 10, we have 5 and 2 are divisible by 6. It proves like n = 6
        else:
            nDistinct = total - a ** 5 - a ** 2 + a
    print("{} {} {} {}".format(twoOrMoreDistinct, nDistinct, oneDistinct, twoOrMoreDistinct % n == 0))
