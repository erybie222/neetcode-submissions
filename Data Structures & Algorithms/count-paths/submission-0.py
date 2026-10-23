class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solutions = [[0] * n for i in range(m)]
        solutions[m-1][n-1] = 1
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1 ,-1):
                if row == m-1 and col == n-1:
                    continue
                curSum = 0
                if row+1 < m:
                    curSum += solutions[row+1][col]
                if col+1 < n:
                    curSum += solutions[row][col+1]
                solutions[row][col] = curSum
        return solutions[0][0]