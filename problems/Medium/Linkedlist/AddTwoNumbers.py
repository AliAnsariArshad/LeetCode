from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    2. Add Two Numbers
    """

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        """

        root = ListNode(0)
        result = root
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            result.next = ListNode(carry%10)
            result = result.next
            carry = carry//10

        return root.next


s = Solution()
l1 = ListNode(243)
l2 = ListNode(564)
print((s.add_two_numbers(l1, l2)))
