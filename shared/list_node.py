from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


def print_list_node(l):
    s = ""
    while l:
        s += str(l.val)
        l = l.next
    print(s)


def to_list_node(array) -> Optional[ListNode]:
    n: Optional[ListNode] = None
    head = ListNode()
    for x in array:
        if not n:
            n = ListNode(x)
            head.next = n
        else:
            n.next = ListNode(x)
            n = n.next
    return head.next


def is_equal(n1: Optional[ListNode], n2: Optional[ListNode]) -> bool:
    if not n1 or not n2:
        return not n1 and not n2

    if n1.val != n2.val:
        return False

    while n1.next:
        if not n2.next:
            return False
        if n1.next.val != n2.next.val:
            return False
        n1 = n1.next
        n2 = n2.next

    if n2.next:
        return False

    return True
