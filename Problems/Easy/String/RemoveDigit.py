import copy


class Solution:
    def remove_digit(self, number: str, digit: str) -> str:
        ls = []
        result = []
        for i, digits in enumerate(number):
            ls.append((i, digits))
        re = list(number)

        for ind, sep in ls:
            if sep == digit:
                rs = copy.copy(re)
                rs.pop(ind)
                result.append(int("".join(rs)))

        return str(max(result))


    def remove_digit2(self, number: str, digit: str) -> str:
        result = []

        for i in range(len(number)):
            if number[i] == digit:
                result.append(int(number[0:i] + number[i+1:]))
        return str(max(result))


s = Solution()
print(s.remove_digit2(number="551", digit="5"))
