from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(nums):
            d[v] = i

        for i, v in enumerate(nums):
            if target - v in d and d[target - v] != i:
                return [i, d[target - v]]

        raise Exception("invalid case")
