class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        else:
            def house_robber(i, j):
                rob1, rob2 = 0 , 0
                for i in range(i,j):
                    temp= max(rob1 + nums[i], rob2)
                    rob1 = rob2
                    rob2= temp
                return rob2

            robber1 = house_robber(0,len(nums)-1)
            robber2 = house_robber(1, len(nums))
            return max(robber1, robber2)
        