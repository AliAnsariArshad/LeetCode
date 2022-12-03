import time


class Solution:
    def remove_duplicates(self, s: str) -> str:
        start_time = time.time()
        stack = []

        for char in s:
            if not char in stack:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        end_time = time.time()
        print(end_time - start_time)
        return "".join(stack)


    def remove_duplicates2(self, s: str) -> str:

        start_time = time.time()
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        end_time = time.time()
        print(end_time-start_time)
        return "".join(stack)








ss = Solution()
# print(ss.remove_duplicates("abbaca"))
# print(ss.remove_duplicates("azxxzy"))
# print(ss.remove_duplicates("aababaab"))
print(ss.remove_duplicates("abbbabaaa"))
print(ss.remove_duplicates2("abbbabaaa"))