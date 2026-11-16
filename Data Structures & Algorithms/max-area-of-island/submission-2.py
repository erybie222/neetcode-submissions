class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = collections.deque()
            curArea = 1
            q.append((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1] ]
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < ROWS and  0 <= c < COLS and grid[r][c] == 1:
                        q.append((r, c))
                        grid[r][c] = 0
                        curArea += 1
            return curArea

                    
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c):
                    grid[r][c] = 0
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea