class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l, r = 0 , 0
        used = set()

        while r < len(s):
            if s[r] not in used:
                used.add(s[r])
                maxLength = max(maxLength, len(used))
                r += 1
            else:
                used.remove(s[l])
                l += 1

        return maxLength