"""https://leetcode.com/problems/regular-expression-matching/"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base case: if p is fully consumed, match iff s is also fully consumed
        if not p:
            return True if not s else False

        # match the first character
        init_match = s[0] == p[0] or p[0] == "." if s else False

        # recursive case: handling the star
        if len(p) > 1 and p[1] == "*":
            # 1. the star matches 0 times (consume the star pattern: p[2:])
            # 2. the star matches 1+ times (consume the string: s[1:])
            return self.isMatch(s, p[2:]) or (init_match and self.isMatch(s[1:], p))

        # non-star case (consume both string and pattern)
        else:
            return init_match and self.isMatch(s[1:], p[1:])
