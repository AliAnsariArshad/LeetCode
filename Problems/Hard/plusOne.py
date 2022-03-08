class Solution:
    """
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer. The digits are ordered
    from most significant to least significant in left-to-right order. The large
    integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
    """

    def plus_one(self, digits):
        """

        :param digits: accept digits array from user
        :return: new digits array
        """
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
