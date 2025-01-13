"""https://leetcode.com/problems/longest-palindromic-substring/"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        # view is the length of the window inspecting the string. going
        # backwards will give the longest palindrome on the first hit
        for view in range(len_s, 1, -1):
            for lhs in range(len_s):
                rhs = lhs + view
                if rhs > len_s:  # rhs of view has gone beyond the string
                    break
                if s[lhs:rhs] == s[lhs:rhs][::-1]:  # reverse string by slice
                    return s[lhs:rhs]
        return s[0]  # length of 1 is the longest
