class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cWater, mWater = 0, 0

        l, r = 0, len(heights) - 1

        while l < r:
            cWater = min(heights[l], heights[r]) * (r - l)
            mWater = max(cWater, mWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mWater