class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        return str(bin(x + y).replace("0b", ""))

    def addBinary2(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        # while y:
        ans = x ^ y
        carry = (x & y) << 1
        if carry == 0:
            return f"{ans}"
        return f"{self.addBinary2(bin(ans), bin(carry))}"
        #     x, y = ans, carry
        #     print(f"x = {x:b} y = {y:b}")
        # return f"{ans:b}"

    def addBinary3(self, a: str, b: str) -> str:
        res = ''
        carry = 0

        # reverse the strings
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            intA = int(a[i]) if i < len(a) else 0
            intB = int(b[i]) if i < len(b) else 0

            newInt = intA + intB + carry
            res = str(newInt % 2) + res
            carry = newInt // 2

        if carry: res = '1' + res

        return res

s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary2("1", "0"))
print(s.addBinary3("1", "0"))
