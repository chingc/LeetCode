"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        score = 0
        hiscore = 0
        maxscore = len(s)

        for i in range(maxscore):
            for c in s[i:]:
                if c in tracker:
                    break
                else:
                    tracker.add(c)
                    score += 1

            if score > hiscore:
                hiscore = score

            if i + hiscore >= maxscore:
                break

            tracker.clear()
            score = 0

        return hiscore
