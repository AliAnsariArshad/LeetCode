class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        new_list = nums1 + nums2
        new_list.sort()
        new_list_len = len(new_list)
        n = int(new_list_len % 2)
        m = int(new_list_len / 2)
        if n == 0:
            return (new_list[m - 1] + new_list[m]) / 2
        else:
            return new_list[m]

    def findMedianSortedArrays2(self, nums1, nums2):
        nums = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))

        if nums1:
            nums = nums + nums1
        if nums2:
            nums = nums + nums2

        total_l = len(nums)
        if total_l % 2 == 0:
            return (nums[total_l // 2 - 1] + nums[total_l // 2]) / 2
        else:
            return nums[total_l // 2]

