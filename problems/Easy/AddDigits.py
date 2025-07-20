class Solution:
    """
    Given an integer num, repeatedly add all its digits until the result has
    only one digit, and return it.
    """

    def addDigits(self, num: int) -> int:
        """
        :param num: receives integer from user
        :return: returns sum of all digits in number in single digits
        """

        while num > 9:
            n = num % 10
            num = num // 10
            num = num + n

        return num
