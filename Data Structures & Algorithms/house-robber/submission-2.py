class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) < 2:
            return nums[0]

        rob = [0 for i in range(len(nums))]
        
       
        rob[-1], rob[-2] = nums[-1], nums[-2]

        for i in range(len(nums) -3, -1, -1):
            if i+3 < len(nums):
                rob[i] = nums[i] + max(rob[i+2], rob[i+3])
            else:
                rob[i] = nums[i] + max(rob[i+2], 0)
            rob[i-1] = nums[i-1] + max(rob[i+1], rob[i+2])

        return max(rob[0], rob[1])
        
