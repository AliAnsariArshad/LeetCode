from typing import List


class Solution:
    def minimum_abs_difference(self, arr: List[int]) -> List[List[int]]:
        d = {}
        result = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                d[(arr[i], arr[j])] = abs(arr[i] - arr[j])
        x = min(d.values())
        for item in d:
            if d[item] == x:
                result.append(list(sorted(item)))
        result.sort()
        return result

    def minimum_abs_difference2(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        a, b = arr[0], arr[1]
        diff = b - a
        result = [[a, b]]

        for i in range(1, len(arr) - 1):
            diff2 = arr[i + 1] - arr[i]
            if diff2 == diff:
                result.append([arr[i], arr[i + 1]])
            elif diff2 < diff:
                diff = diff2
                result = [[arr[i], arr[i + 1]]]
        return result


s = Solution()
print(s.minimum_abs_difference(arr=[4, 2, 1, 3]))
print(s.minimum_abs_difference2(arr=[4, 2, 1, 3]))
