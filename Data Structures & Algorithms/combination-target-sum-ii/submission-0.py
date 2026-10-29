class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur,total):
            if total == target:
                res.append(cur.copy())
                return
            elif i >= len(candidates) or total > target:
                return
            else:
                cur.append(candidates[i])
                dfs(i+1, cur , total + candidates[i])
                last = cur.pop()
                while i < len(candidates) and last == candidates[i]:
                    i+=1
                dfs(i, cur, total)
        dfs(0, [], 0)
        return res