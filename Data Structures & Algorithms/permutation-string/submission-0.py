class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}

        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
        
        l, r = 0, 0

        while r < len(s2):
            countS2[s2[r]] = countS2.get(s2[r], 0) + 1
            windowLen = r - l + 1

            if countS1 == countS2:
                return True
            if windowLen == len(s1):
                val = countS2.get(s2[l])
                if val > 1:
                    countS2[s2[l]] = val - 1
                else:
                    countS2.pop(s2[l])
                l += 1
            
            r += 1

        return False
