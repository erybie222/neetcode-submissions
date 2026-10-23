class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0 , 0
        count = {}
        maxLength = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            windowSize = r - l + 1
            maxCount = max(count.values())
            if windowSize - maxCount > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
                
            windowSize = r - l + 1
            maxLength = max(maxLength, windowSize)
            r += 1      
        return maxLength
