"""https://leetcode.com/problems/string-to-integer-atoi/"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        s = s.strip()

        if not s:
            return num

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        i32_max = 0x7FFFFFFF
        i32_min = -0x80000000

        for c in s:
            if c in "0123456789":
                num = num * 10 + int(c)
                check = num * sign
                if check > i32_max:
                    return i32_max
                if check < i32_min:
                    return i32_min
            else:
                break  # encountered non-digit

        return num * sign
