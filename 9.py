"""https://leetcode.com/problems/palindrome-number/"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # negative sign makes it false
            return False
        elif x < 10:  # single digit always true
            return True
        elif x % 10 == 0:  # divisible by 10 are false
            return False

        # reverse the number and stop once the original is lexically cut in half
        orig = x
        rev = 0
        while orig > rev:
            rev = rev * 10 + orig % 10  # note: first time thru is 0 * 10 + remainder
            orig //= 10  # drop right most digit

        # or case: rev has an extra digit if orig had an odd number
        # of digits. it can be dropped because it's the pivot point
        return orig == rev or orig == rev // 10
