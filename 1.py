"""https://leetcode.com/problems/two-sum/"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, x in enumerate(nums):
            # slice the list after index i
            for j, y in enumerate(nums[i + 1 :], start=1):
                if x + y == target:
                    return [i, i + j]
        return []  # no solution
