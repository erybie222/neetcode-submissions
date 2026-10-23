class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target or i >= len(nums):
                return
            else:
                dfs(i, cur.copy() + [nums[i]], total+ nums[i])
                dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
       