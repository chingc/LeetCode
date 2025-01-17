"""https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/"""


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        results = set()
        tracker = {}
        for lhs in range(len(s)):
            for rhs in range(lhs, len(s)):
                if s[rhs] in tracker:
                    tracker[s[rhs]] += 1
                else:
                    tracker[s[rhs]] = 1
                if len(set(tracker.values())) == 1:
                    results.add(s[lhs : rhs + 1])
            tracker.clear()
        return len(results)
