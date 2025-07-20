def sellbuy(price):
    out = 0
    temp = 0
    outlist = []
    for i in range(len(price)-1):
        for j in range(i+1, len(price)):
            temp = price[j] - price[i]
            if temp >= 0:
                outlist.append(temp)
    outlist.sort()
    if outlist:
        if outlist[-1] > out:
            return outlist[-1]
    else:
        return out


# print(sellbuy([7,1,5,3,6,4]))
# print(sellbuy([7,6,4,3,1]))
print(sellbuy([3,3]))
