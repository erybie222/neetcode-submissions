class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue  # ta sama wartość na tym samym poziomie = duplikat
                if total + candidates[j] > target:
                    break     # posortowane, więc dalej będzie tylko gorzej
                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()

        dfs(0, [], 0)
        return res