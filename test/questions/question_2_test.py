import unittest
from questions.question_2 import solution
from shared.list_node import to_list_node, is_equal


class TestSolution(unittest.TestCase):
    def test_solution(self):
        cases = [
            (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
            (([0], [0]), [0]),
            (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
            (([2, 4, 3], []), [2, 4, 3]),
        ]
        for (left, right), expected in cases:
            with self.subTest((left, right)):
                s = solution.Solution()
                self.assertTrue(
                    is_equal(
                        to_list_node(expected),
                        s.addTwoNumbers(to_list_node(left), to_list_node(right)),
                    )
                )
