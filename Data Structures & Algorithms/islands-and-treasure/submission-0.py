class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        inf = 2**31 - 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
            
        
        while q:    
            row, col = q.popleft()

            directions = [[-1, 0 ], [1, 0], [0, -1], [0, 1]]
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r < 0 or c < 0 or rows <= r or cols <= c:
                    continue
                if grid[r][c] == inf:
                    grid[r][c] = grid[row][col] + 1
                    q.append((r, c))

       
            
