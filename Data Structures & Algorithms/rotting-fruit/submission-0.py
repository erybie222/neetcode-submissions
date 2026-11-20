class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            t = grid[r][c]                      
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = t + 1        
                    fresh -= 1
                    minutes = t + 1 - 2
                    q.append((nr, nc))

        return minutes if fresh == 0 else -1