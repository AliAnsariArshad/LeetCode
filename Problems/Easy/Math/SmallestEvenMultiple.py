class Solution:
    def smallest_even_multiple(self, n: int) -> int:
        # if n % 2 == 0:
        #     return n
        # else:
        #     return 2 * n

        return n if n % 2 == 0 else 2 * n

