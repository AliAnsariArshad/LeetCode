class Solution:
    def find_kth_bit(self, n: int, k: int) -> str:
        result = "0"

        if n == 1:
            return result

        for i in range(1, n):
            rs = ""
            # for char in result:
            #     if char == "0":
            #         rs += "1"
            #     elif char == "1":
            #         rs += "0"
            rv = ["1" if x == "0" else "0" for x in result][::-1]
            ss = "".join(rv)
            result = result + "1" + ss

        return str(result[k-1])



s = Solution()
print(s.find_kth_bit(n=4, k=11))
