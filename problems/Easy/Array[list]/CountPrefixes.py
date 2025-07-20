from typing import List


class Solution:
    def count_prefixes(self, words: List[str], s: str) -> int:
        count = 0
        # for i in range(len(l)):
        #     if not newlist:
        #         newlist.append(l[i])
        #     else:
        #         temp = newlist[len(newlist)-1]
        #         temp = temp +l[i]
        #         newlist.append(temp)

        for char in words:
                n = len(char)
                pre = s[0:n]
                if pre == char:
                    count += 1

        return count

    def count_prefixes2(self, words: List[str], s: str) -> int:
        return sum(map(s.startswith, words))

    def count_prefixes3(self, words: List[str], s: str) -> int:
        count = 0
        for char in words:
            if s[:len(char)] == char:
                count += 1
        return count

    def count_prefixes4(self, words: List[str], s: str) -> int:
        l = list(s)
        newlist = []
        count = 0
        for i in range(len(l)):
            if not newlist:
                newlist.append(l[i])
            else:
                temp = newlist[len(newlist)-1]
                temp = temp +l[i]
                newlist.append(temp)

        for word in words:
            if word in newlist:
                count += 1

        return count

    def count_prefixes5(self, words: List[str], s: str) -> int:
        newlist = []
        count = 0
        for i in range(len(s)):
            newlist.append(s[0:i+1])

        for word in words:
            if word in newlist:
                count += 1

        return count


s = Solution()
# print(s.count_prefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
# print(s.count_prefixes(words=["a", "a"], s="aa"))
#
# print(s.count_prefixes2(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
# print(s.count_prefixes2(words=["a", "a"], s="aa"))
#
# print(s.count_prefixes3(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
# print(s.count_prefixes3(words=["a", "a"], s="aa"))

print(s.count_prefixes4(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
print(s.count_prefixes4(words=["a", "a"], s="aa"))
print(s.count_prefixes5(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
print(s.count_prefixes5(words=["a", "a"], s="aa"))
