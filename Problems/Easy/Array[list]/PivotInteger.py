class Solution:
    """
    2485. Find the Pivot Integer
    """
    def pivot_integer(self, n: int) -> int:

        arr = [x for x in range(1, n + 1)]
        i = 0
        while i < len(arr):
            a = sum(arr[:i+1])
            b = sum(arr[i:len(arr) + 1])
            if a != b:
                i += 1
                continue
            else:
                return arr[i]
        return -1

    def pivot_integer2(self, n: int) -> int:
        prefix = 0
        suffix = sum(range(1, n + 1))
        for x in range(1, n + 1):
            prefix += x
            if prefix == suffix:
                return x
            suffix -= x
        return -1


s = Solution()
# print(s.pivot_integer(n=8))
# print(s.pivot_integer(n=4))
print(s.pivot_integer2(n=8))
print(s.pivot_integer2(n=4))
