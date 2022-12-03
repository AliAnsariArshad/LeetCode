class Solution:
    def is_isomporphic(self, s: str, t: str):
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))

    def is_list_isomorphic(self, ls: list):
        new_list = []
        for i in range(len(ls) - 1):
            for j in range(i+1, len(ls) - 1):
                if len(ls[i]) == len(ls[j]):
                    if len(set(ls[i])) == len(set(zip(ls[i], ls[j]))) == len(set(ls[j])):
                        if ls[i] not in new_list:
                            new_list.append(ls[i])
                        if ls[j] not in new_list:
                            new_list.append(ls[j])
        if new_list:
           return new_list
        else:
            return "there are no isomorphic strings"

    def is_isomorphic2(self, s: str, t: str) -> bool:
        matches = {}
        first = False
        second = False
        i = 0
        while i < len(s):
            if s[i] not in matches:
                matches[s[i]] = t[i]  # match the letter on the same spot if not seen

            if matches[s[i]] != t[i]:
                break
            i += 1

        first = (i == len(s))

        matches = {}
        i = 0
        while i < len(t):
            if t[i] not in matches:
                matches[t[i]] = s[i]  # match the letter on the same spot if not seen

            if matches[t[i]] != s[i]:
                break
            i += 1
        second = (i == len(s))

        return first and second

    def is_isomorphic3(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        print(d1)
        print(d2)
        return sorted(d1.values()) == sorted(d2.values())


s = Solution()
print(s.is_isomorphic3("egg", "add"))
print(s.is_isomporphic("foo", "bar"))
print(s.is_list_isomorphic(["fosdfsdfsdfor", "barsfdsfe", "egsdfsdfsdfgf", "adsdfsdfsds", "apple"]))
