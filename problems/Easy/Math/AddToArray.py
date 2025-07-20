from typing import List


class Solution:
    def add_to_array(self, num: List[int], k: int) -> List[int]:
        strlist = [str(i) for i in num]
        result = ''.join(strlist)
        finalresult = str(int(result) + k)

        return [int(i) for i in finalresult]

    def add_to_array2(self, num: List[int], k: int) -> List[int]:
        result = list(str(int(''.join([str(i) for i in num]))+k))

        return [int(i) for i in result]

    def add_to_array3(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        i = len(num) - 1
        while i > 0 and num[i] > 9:
            num[i-1] += num[i]//10
            num[i] = num[i]%10
            i -= 1
        while num[0] > 9:
            num = [num[0]//10] + num
            num[1] = num[1]%10

        return num



s = Solution()
print(s.add_to_array3(num=[1, 2, 0, 0], k=1))
