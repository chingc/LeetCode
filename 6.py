"""https://leetcode.com/problems/zigzag-conversion/"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [i for i in range(numRows)]
        zigzag.extend([i for i in range(numRows - 2, 0, -1)])
        while len(zigzag) < len(s):
            zigzag *= 2

        parts = ["" for _ in range(numRows)]
        for i, c in zip(zigzag, s):
            parts[i] += c

        return "".join(parts)
