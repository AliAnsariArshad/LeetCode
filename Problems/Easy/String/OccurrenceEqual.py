from collections import Counter


class Solution:
    def are_occurrences_equal(self, s: str) -> bool:
        d = dict(Counter(s))
        s = set()
        for key in d:
            s.add(d[key])
        return True if len(s) == 1 else False

    def are_occurrences_equal2(self, s: str)-> bool:
        d = Counter(s)
        vals = set(d.values())
        return len(vals) == 1

    def are_occurrences_equal3(self, s: str)-> bool:
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        return len(set(counter.values())) == 1


s = Solution()
print(s.are_occurrences_equal("abacbc"))
print(s.are_occurrences_equal("aaabb"))

print(s.are_occurrences_equal2("abacbc"))
print(s.are_occurrences_equal2("aaabb"))

print(s.are_occurrences_equal3("abacbc"))
print(s.are_occurrences_equal3("aaabb"))