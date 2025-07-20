class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        w1 = set(word1)
        w2 = set(word2)
        if w1 != w2:
            return False

        n = len(w1)

        arr1 = [0] * n
        arr2 = [0] * n
        c1 = 0
        c2 = 0

        for i in w1:
            arr1[c1] = word1.count(i)
            c1 += 1

        for j in w2:
            arr2[c2] = word2.count(j)
            c2 += 1
        arr1.sort()
        arr2.sort()
        return True if arr1 == arr2 else False


s = Solution()
print(s.closeStrings(word1='cabbba', word2='abbccc'))
print(s.closeStrings(word1='abbzzca', word2='babzzcz'))



