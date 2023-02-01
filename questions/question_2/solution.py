from typing import Optional
from shared.list_node import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        n: Optional[ListNode] = None
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()

            total = l1.val + l2.val + carry
            v = total % 10
            carry = 1 if total > 9 else 0
            if not n:
                n = ListNode(v, None)
                head.next = n
            else:
                n.next = ListNode(v, None)
                n = n.next
            l1 = l1.next
            l2 = l2.next

        assert n

        if carry:
            n.next = ListNode(carry, None)

        return head.next
