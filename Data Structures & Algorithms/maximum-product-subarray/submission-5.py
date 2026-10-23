class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            curMin, curMax = min(curMin * n, curMax * n, n), max(curMin * n, curMax * n, n)
            res = max(res, curMax,)
        return res