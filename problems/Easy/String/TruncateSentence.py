class Solution:
    def truncate_sentence(self, s, k):
        sentence_list = s.split(" ")
        result = []
        for i in range(0, k):
            result.append(sentence_list[i])
        return " ".join(result)

    def truncate_sentence2(self, s, k):
        return " ".join(s.split(" ")[:k])

st = Solution()
print(st.truncate_sentence("What is the solution to this problem", 4))
print(st.truncate_sentence2("What is the solution to this problem", 4))
