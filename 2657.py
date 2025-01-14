"""https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/"""


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        pca = []
        for i in range(1, len(A) + 1):
            pca.append(len(set(A[:i]) & set(B[:i])))
        return pca
