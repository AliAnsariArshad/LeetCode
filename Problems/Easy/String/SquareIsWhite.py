class Solution:
    def is_square_white(self, s):
        even, odd = ['b', 'd', 'f', 'h'], ['a', 'c', 'e', 'g']

        if s[0] in even:
            if int(s[-1]) % 2 == 0:
                return False
            return True
        else:
            if int(s[-1]) % 2 != 0:
                return False
            return True


st = Solution()
print(st.is_square_white('b3'))
