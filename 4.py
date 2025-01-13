"""https://leetcode.com/problems/median-of-two-sorted-arrays/"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        q, r = divmod(len(nums1), 2)
        if r:
            return nums1[q]
        return (nums1[q - 1] + nums1[q]) / 2
