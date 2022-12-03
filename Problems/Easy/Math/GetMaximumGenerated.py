class Solution:
    def get_maximum_generated(self, n: int) -> int:
        ls = [0] * (n + 2)
        ls[1] = 1
        for i in range(2, n + 1):
            ls[i] = ls[i // 2] + ls[(i // 2) + 1] * (i % 2)
        print(ls)
        return max(ls[:n + 1])

    def get_maximum_generated2(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        ls = [0] * (n + 1)
        ls[1] = 1
        i = 2
        while i <= n:
            if i%2 == 0:
                ls[i] = ls[i//2]
            else:
                ls[i] = ls[i//2] + ls[(i//2)+1]
            i += 1
        return max(ls)


s = Solution()
print(s.get_maximum_generated(n=7))
print(s.get_maximum_generated2(n=100))
