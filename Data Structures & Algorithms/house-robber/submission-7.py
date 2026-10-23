class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        rob = [0 for i in range(len(nums))]
        
        rob[0], rob[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob[i] = max(rob[i-2] + nums[i], rob[i-1])
        
        return rob[-1]
        
