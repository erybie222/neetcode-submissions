class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff = 0
        for i in range(len(nums)):
            diff += i - nums[i]
        diff += len(nums)
        return diff
