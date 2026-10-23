class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i >= rows or j<0 or j >= cols:
                return
            if grid[i][j] == "1" and (i,j) not in visited:
                visited.add((i,j))
                return (dfs(i+1,j) or dfs(i-1,j) or dfs(i,j+1) or dfs(i,j-1)) 
            return False
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    counter += 1
                    dfs(i,j)
        return counter
        


