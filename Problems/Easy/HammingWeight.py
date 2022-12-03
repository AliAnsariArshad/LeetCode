def hammingWeight(self, n: int) -> int:
    num = str(n)
    count = 0
    for i in range(len(num) - 1):
        if num[i] == 1:
            count += 1
    return count

print(hammingWeight(0o00000000000000000000000000001011))