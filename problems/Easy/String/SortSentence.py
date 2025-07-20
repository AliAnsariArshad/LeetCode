class Solution:
    def sort_sentence(self, sentence):
        sentence_list = sentence.split(" ")
        d = {}
        result = ""
        for char in sentence_list:
            d[char[-1]] = char[:-1]
        # d.
        # print(len(d))

        for i in range(1, len(d)+1):
            result = result + d[str(i)] + " "
        return result.rstrip(" ")

    def sort_sentence2(self, sentence):
        l = sentence.split()
        l = sorted(l, key=lambda i: int(i[-1]))
        l = [i[:-1] for i in l]
        return ' '.join(l)




s = Solution()
print(s.sort_sentence("sentence4 a3 is2 This1"))
print(s.sort_sentence2("sentence4 a3 is2 This1"))