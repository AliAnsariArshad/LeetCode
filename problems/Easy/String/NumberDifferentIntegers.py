class Solution:
    def num_differente_integer(self, s):
        num = ""
        num_list = []

        for char in s:
            if char.isdigit():
                num = num + char
            else:
                if num:
                    num_list.append(num.lstrip("0"))
                    num = ""
        if num.isdigit():
            num_list.append(num.lstrip("0"))
        int_num = set(num_list)
        return len(int_num)

    def num_diferent_integers(self, word: str) -> int:
        def is_alpha(c) -> bool:
            if ord('a') <= ord(c) <= ord('z'):
                return True
            return False

        temp = ""
        ss = set()
        for c in word:
            if not is_alpha(c):
                temp += str(c)
            else:
                if temp:
                    # print(temp)
                    ss.add(int(temp))
                temp = ""
        if temp:
            ss.add(int(temp))
        # print(ss)
        return len(ss)


s = Solution()
print(s.num_differente_integer("a123bc34d8ef34"))
print(s.num_differente_integer("leet1234code234"))
print(s.num_differente_integer("a1b01c001"))

print(s.num_diferent_integers("a123bc34d8ef34"))
print(s.num_diferent_integers("leet1234code234"))
print(s.num_diferent_integers("a1b01c001"))

