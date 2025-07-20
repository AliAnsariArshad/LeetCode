class Solution:
    def minimum_moves(self, s: str) -> int:
        if 'X' not in s:
            return 0
        else:
            if len(s)%3 == 0:
                return len(s)//3
            else:
                return len(s) // 3 + 1

    def minimum_moves2(self, s: str) -> int:
        s += "OOO"

        i, result = 0, 0

        while i < len(s) - 3:
            window = s[i:i + 3]
            if window in ["XOX", "XXX", "XOO", "XXO"]:
                i += 3
                result += 1
            else:
                i += 1
        return result

    def minimum_moves3(self, s: str) -> int:
        result = i = 0
        while i < len(s):
            if s[i] == 'X':
                result += 1
                i += 3
            else:
                i += 1
        return result

    def minimum_moves4(self, s: str) -> int:
        result = i = 0
        while i < len(s):
            if s[i] == 'X':
                result += 1
                i += 3
                continue
            i += 1
        return result




ss = Solution()
print(ss.minimum_moves("XXOX"))
print(ss.minimum_moves("XXX"))

# print(ss.minimum_moves2("XXOX"))
# print(ss.minimum_moves2("XXX"))
print(ss.minimum_moves2("OOO"))


print(ss.minimum_moves3("OOO"))
print(ss.minimum_moves4("OOO"))
