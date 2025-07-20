class Solution:
    def is_palindrome(self, s: str):
        st = ""
        for char in s:
            if char.isalpha():
                st += char.lower()
            if char.isnumeric():
                st += char
        return st == st[::-1]

    def is_palindromes(self, s: str):
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        return new_string == new_string[::-1]
        # left, right = 0, len(new_string)-1
        # while left < right:
        #     if new_string[left] == new_string[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True



s = Solution()
print(s.is_palindrome("A man, a plan, a canal: Panama"))
print(s.is_palindromes("A mn, a plan, a canal: Panama"))