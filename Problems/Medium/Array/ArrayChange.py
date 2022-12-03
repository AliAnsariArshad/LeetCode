from typing import List


class Solution:
    """
    2295. Replace Elements in an Array
    """

    def array_change(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """

        @param nums:
        @type nums:
        @param operations:
        @type operations:
        @return:
        @rtype:
        """

        for item in operations:
            a = item[0]
            b = item[1]
            if a in nums:
                nums[nums.index(a)] = b

        return nums

    def array_change2(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """

        @param nums:
        @type nums:
        @param operations:
        @type operations:
        @return:
        @rtype:
        """

        d = {num: i for i, num in enumerate(nums)}
        for s, e in operations:
            i = d[s]
            nums[i] = e
            d[e] = i
            del d[s]
        return nums

    def array_change3(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        ops = dict()
        for key, val in reversed(operations):
            ops[key] = ops.get(val, val)
        return (ops.get(num, num) for num in nums)

    def array_change4(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        """

        @param nums:
        @type nums:
        @param operations:
        @type operations:
        @return:
        @rtype:
        """

        d = dict(zip(nums, range(len(nums))))
        for item in operations:
            e = d[item[0]]
            del d[item[0]]
            d[item[1]] = e
        return sorted(d.keys(), key=lambda x: d[x])


s = Solution()
print(s.array_change(nums=[1, 2], operations=[[1, 3], [2, 1], [3, 2]]))
print(s.array_change2(nums=[1, 2], operations=[[1, 3], [2, 1], [3, 2]]))
print(s.array_change3(nums=[1, 2], operations=[[1, 3], [2, 1], [3, 2]]))
print(s.array_change4(nums=[1, 2], operations=[[1, 3], [2, 1], [3, 2]]))
