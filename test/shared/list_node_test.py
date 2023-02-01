from shared.list_node import ListNode, is_equal, to_list_node
from unittest import TestCase


class TestIsEqual(TestCase):
    def testCases(self):
        cases = [
            ("should return True when both is None", None, None, True),
            ("should return False when one is None", ListNode(1), None, False),
            (
                "should return True when both is single Node with same value",
                ListNode(1),
                ListNode(1),
                True,
            ),
            (
                "should return False when both is single Node with different value",
                ListNode(1),
                ListNode(2),
                False,
            ),
            (
                "should return True when both is multi Nodes",
                ListNode(1, ListNode(2)),
                ListNode(1, ListNode(2)),
                True,
            ),
            (
                "should return False when both is multi Nodes with different value",
                ListNode(1, ListNode(3)),
                ListNode(1, ListNode(2)),
                False,
            ),
            (
                "should return False when left is longer than right",
                ListNode(1, ListNode(2, ListNode(3))),
                ListNode(1, ListNode(2)),
                False,
            ),
            (
                "should return False when right is longer than left",
                ListNode(1, ListNode(2)),
                ListNode(1, ListNode(2, ListNode(3))),
                False,
            ),
        ]
        for case_name, left, right, expected in cases:
            with self.subTest(case_name):
                self.assertEqual(expected, is_equal(left, right))


class TestListNode(TestCase):
    def testToListNode(self):
        cases = [([2, 4, 3], ListNode(2, ListNode(4, ListNode(3))))]
        for input, expected in cases:
            with self.subTest(input):
                self.assertTrue(is_equal(expected, to_list_node(input)))
