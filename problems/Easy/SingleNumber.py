def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i


def singleNumberII(nums):
    new = set(nums)
    new2 = sum(nums)
    var = 2 * sum(new)
    var2 = var - new2

    return var2


def singleNumberIII(nums):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for num, count in dict.items():
        if count == 1:
            return num


def func(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


print(func([1, 0, 2, 3], 3))

print(singleNumber([2, 2, 3, 2]))
