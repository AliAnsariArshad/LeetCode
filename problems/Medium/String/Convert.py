class Solution:
    """
    6. Zigzag Conversion
    """

    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        """

        :param s: string
        :type s: str
        :param num_rows: number of rows
        :type num_rows: int
        :return: str
        :rtype: str
        """

        if num_rows == 1 or num_rows > len(s):  # corner case
            return s
        res, i, step = ['' for r in range(num_rows)], 0, 0  # a string for each line
        for char in s:
            res[i] += char
            if i == 0:  # first row
                step = 1  # down
            if i == num_rows - 1:  # last row
                step = -1  # up
            i += step
        return "".join(res)


ss = Solution()
print(ss.convert(s="PAYPALISHIRING", num_rows=4))
