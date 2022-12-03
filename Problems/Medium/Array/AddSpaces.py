from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        old_index = 0

        for index in spaces:
            z = s[old_index:index]
            arr.append(z)
            old_index = index
        arr.append(s[old_index: len(s)])
        return " ".join(arr)

    def addSpaces2(self, s: str, spaces: List[int]) -> str:
        arr = []
        old_index = 0

        for index in spaces:
            arr.append(s[old_index:index])
            old_index = index
        arr.append(s[old_index:])
        return " ".join(arr)


ss = Solution()
print(ss.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]))
print(ss.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
print(ss.addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))


print(ss.addSpaces2(s="icodeinpython", spaces=[1, 5, 7, 9]))
print(ss.addSpaces2(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
print(ss.addSpaces2(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))
