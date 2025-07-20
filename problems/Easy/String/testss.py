ls = [9, 1, 2, 5, 7, 4, 9, 0, 8]
for i in range(len(ls) - 1):
    checkvalue = ls[i]
    for j in range(i + 1, len(ls) - 1):
        checkvalue2 = ls[j]
        if ls[i] > ls[j]:
            a = ls[i]
            ls[i] = ls[j]
            ls[j] = a

print(ls)