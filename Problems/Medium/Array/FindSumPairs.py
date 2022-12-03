from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans = []
        for i in range(len(self.nums1)):
            for j in range(len(self.nums2)):
                if self.nums1[i] + self.nums2[j] == tot:
                    ans.append((self.nums1[i], self.nums2[j]))
        return len(ans)


ss = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(ss.count(7))