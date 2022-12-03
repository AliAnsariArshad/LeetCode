import collections


class Solution:
    def frequencySort(self, s: str) -> str:

        d = {}
        sss =''
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        dd = list(d.items())
        dd.sort(key=lambda x: x[1], reverse=True)

        for item in dd:
            temp = item[0]*item[1]
            sss +=temp

        return sss

    def frequencySort2(self, s: str) -> str:
        sss =''
        dd = collections.Counter(s)
        ll = list(tuple(dd.items()))
        ll.sort(key=lambda x: x[1], reverse=True)

        for item in ll:
            temp = item[0]*item[1]
            sss +=temp

        return sss


ss = Solution()
print(ss.frequencySort(s='tree'))
print(ss.frequencySort(s='cccaaa'))
print(ss.frequencySort(s='Aabb'))

print(ss.frequencySort2(s='tree'))
print(ss.frequencySort2(s='cccaaa'))
print(ss.frequencySort2(s='Aabb'))