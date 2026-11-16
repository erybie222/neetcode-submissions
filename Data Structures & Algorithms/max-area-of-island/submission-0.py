class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = collections.deque()
            curArea = 1
            q.append((r, c))
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1] ]
            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                        q.append((r, c))
                        visited.add((r,c))
                        curArea += 1
            return curArea

                    
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea