import string
from collections import Counter


class Solution:
    def is_panagram(self, sentence):
        newset = set(sentence)
        return len(newset) == 26

    def is_panagram1(self, sentence):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for char in alpha:
            if char not in sentence:
                return False
        return True

    def is_panagram2(self, sentence):
        alpha_dict = {}
        for char in sentence:
            if char not in alpha_dict:
                alpha_dict[char] = 1
        return len(alpha_dict.keys()) == 26

    def is_panagram3(self, sentence):
        alpha_list = []
        for char in sentence:
            if char not in alpha_list:
                alpha_list.append(char)
        return len(alpha_list) == 26

    def is_panagram4(self, sentence):
        alpha_list = [0]*26
        for char in sentence:
            alpha_list[ord(char)- 97 ] = 1
        if alpha_list.count(0):
            return False
        return True

    def checkIfPangram(self, sentence: str) -> bool:
        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
        return True

s = Solution()
print(s.is_panagram("thequickbrownfoxjumpsoverthelazydog"))
print(s.is_panagram("leetcode"))
print(s.is_panagram1("thequickbrownfoxjumpsoverthelazydog"))
print(s.is_panagram1("leetcode"))

print(s.is_panagram2("thequickbrownfoxjumpsoverthelazydog"))
print(s.is_panagram2("leetcode"))
print(s.is_panagram3("thequickbrownfoxjumpsoverthelazydog"))
print(s.is_panagram3("leetcode"))
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram("leetcode"))

