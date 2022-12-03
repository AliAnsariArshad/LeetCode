class Solution:

    def contains_nearby_duplicates(self, nums, k):

        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                new_lsit = d[nums[i]]
                new_lsit.append(i)

                d[nums[i]] = new_lsit

        nextlist = []
        for key in d:
            if len(d[key]) > 1:
                for i in range(len(d[key]) - 1):
                    for j in range(i + 1, len(d[key])):
                        nextlist.append(abs(d[key][i] - d[key][j]))
            # print(nextlist)
            flag = True
            for num in nextlist:
                if num <= k:
                    continue
                else:
                    flag = False
            return flag

    def contains_nearby_duplicate2(self, nums, k):
        lookup = {}

        for i in range(len(nums)):

            # If num is present in lookup and satisfy the condition return True
            if nums[i] in lookup and abs(lookup[nums[i]] - i) <= k:
                return True

            # If num is not present in lookup then add it to lookup
            lookup[nums[i]] = i

        return False

    def contains_nearby_duplicates4(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                dic[nums[i]] = i
        return False


s = Solution()
# print(s.contains_nearby_duplicates([99,99], 2))
print(s.contains_nearby_duplicates4([1,2,3,1], 3))
# print(s.contains_nearby_duplicates([1,2,3,1], 3))
