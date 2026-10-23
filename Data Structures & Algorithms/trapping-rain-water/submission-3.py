class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1
        maxL, maxR = 0, 0
        area = 0

        while l < r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)

            if maxL <= maxR:
                l += 1
                area += max(0, min(maxL, maxR)- height[l])

            else:
                r -= 1
                area += max(0, min(maxL, maxR)- height[r])
        return area
