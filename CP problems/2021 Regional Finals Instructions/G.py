s = input()
a = []
for i in s:
    a.append(i)

k = ['A', 'E', 'I', 'O', 'U', 'G', 'L']
k1 = ['G', 'L']
i = 1
while i < len(s):
    if a[i] in k and a[i] not in k1:
        l = i - 1
        while l > 0 and a[l] not in k:
            l -= 1
        if a[l] not in k1:

            a[l] = 'G'
        i += 1
    i += 1

for i in a:
    print(i, end ="")