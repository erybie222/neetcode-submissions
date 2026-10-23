class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for i in range(len(height))]
        maxRight = [0 for i in range(len(height))]
        area = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            maxRight[j] = max(maxRight[j+1], height[j+1])
        for k in range(len(height)):
            minLR = min(maxLeft[k], maxRight[k])
            area += max(0, minLR- height[k])
        return area
