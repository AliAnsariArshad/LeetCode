class Solution:

    def plus_one(self, digits):
        if digits[-1] < 9:
            num = digits[len(digits) - 1] + 1
            digits.pop()
            digits.insert(len(digits), num)
            return digits

        digits[-1] += 1
        i = len(digits) - 1

        while i > 0 and digits[i] > 9:
            digits[i] = digits[i] % 10
            digits[i - 1] += 1
            i -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
