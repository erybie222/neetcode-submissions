class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, lastHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or  lastHeight > heights[r][c]:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])




        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows - 1, c, atlantic, 0)
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols - 1, atlantic, 0)
        
        res = []

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res


        