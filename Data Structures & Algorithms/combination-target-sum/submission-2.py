class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i, curSum):
            if i >= len(nums) or curSum > target:
                return
            elif curSum == target:
                result.append(subset.copy())
                return
            else:
                subset.append(nums[i])
                dfs(i, curSum + nums[i])
                curSum -= subset.pop()
                dfs(i+1, curSum + nums[i])

        dfs(0,0)
        return result