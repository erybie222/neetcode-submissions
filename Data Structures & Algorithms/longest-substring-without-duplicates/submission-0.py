class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        l = 0
        r = 0
        best = 0

        while r < len(s):
            if s[r] not in used:
                used.add(s[r])
                r += 1
                best = max(best, r - l)
            else:
                used.remove(s[l])
                l += 1

        return best