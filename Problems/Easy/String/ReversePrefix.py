class Solution:
    def reverse_prefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch)
            s = word[:index+1][::-1]+word[index+1:]
            return s
        else:
            return word

    def reverse_prefix2(self, word: str, ch: str) -> str:
        prefix = ""
        found = False
        for char in word:
            if char != ch:
                prefix += char
            else:
                prefix += char
                found = True
                break
        if not found:
            return word

        return prefix[::-1]+word[len(prefix):]


ss = Solution()
print(ss.reverse_prefix(word="abcdefd", ch="d"))
print(ss.reverse_prefix(word="xyxzxe", ch="z"))
print(ss.reverse_prefix(word="abcd", ch="z"))

print(ss.reverse_prefix2(word="abcdefd", ch="d"))
print(ss.reverse_prefix2(word="xyxzxe", ch="z"))
print(ss.reverse_prefix2(word="abcd", ch="z"))