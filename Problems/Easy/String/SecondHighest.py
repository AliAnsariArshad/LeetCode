class Solution:
    def second_highest(self, s: str):
        num_list = []
        for char in s:
            if char.isdigit():
                if char not in num_list:
                    num_list.append(char)
        num_list.sort()
        if len(num_list) == 0 or len(num_list) == 1:
            return -1
        else:
            return num_list[len(num_list)-2]

    def second_highest2(self, s: str):
        num_list = []
        for char in s:
            if char.isdigit():
                if char not in num_list:
                    num_list.append(char)
        num_list.sort()
        if len(num_list) < 2:
            return -1
        else:
            return num_list[-2]

st = Solution()
print(st.second_highest2("df23g"))