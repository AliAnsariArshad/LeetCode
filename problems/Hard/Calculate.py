


class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, 1, [0]

        for item in s:
            if item.isdigit():
                num = num*10 + int(item)

            elif item == " ":
                continue

            elif item == "(":
                stack.extend([sign, 0])
                sign = 1
                num = 0
            elif item == "+":
                stack[-1] += num* sign
                sign = 1
                num = 0
            elif item == "-":
                stack[-1] += num * sign
                sign = -1
                num = 0
            elif item ==")":
                result = (stack.pop() + num*sign)* stack.pop()
                stack[-1] += result
                sign = 1
                num = 0

        return stack[-1] + num * sign



ss = Solution()
print(ss.calculate(" (1+(4+5+2)-3)+(6+8) "))
