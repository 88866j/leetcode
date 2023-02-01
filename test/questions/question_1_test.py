import unittest
from questions.question_1 import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        cases = [
            (([2, 7, 11, 15], 9), [0, 1]),
            (([3, 2, 4], 6), [1, 2]),
            (([3, 3], 6), [0, 1]),
        ]
        for (nums, target), expected in cases:
            with self.subTest(nums):
                s = solution.Solution()
                self.assertEqual(expected, s.twoSum(nums, target))
