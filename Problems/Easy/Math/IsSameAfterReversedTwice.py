class Solution:
    def is_same_after_reversec_twice(self, num: int) -> bool:
        result = True
        new_num = str(num)
        new_num1 = int(new_num[::-1])
        new_num2 = str(new_num1)
        new_num3 = int(new_num2[::-1])
        return num == new_num3

    def is_same_after_reversec_twice2(self, num: int) -> bool:
        return num==int(str(int(str(num)[::-1]))[::-1])

    def is_same_after_reversec_twice3(self, num: int) -> bool:
        def reverse_number(n):
            val = 0
            while n > 0:
                val = val * 10 + n % 10
                n = n // 10
            return val

        rev = reverse_number(num)
        return reverse_number(rev) == num


s = Solution()
print(s.is_same_after_reversec_twice3(526))