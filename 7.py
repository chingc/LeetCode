"""https://leetcode.com/problems/reverse-integer/"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        orig = abs(x)
        rev = 0

        while orig > 0:
            rev = rev * 10 + orig % 10  # first time thru is 0 * 10 + remainder
            if rev.bit_length() > 31:  # overflow
                return 0
            orig //= 10  # drop right most digit

        return rev * sign
