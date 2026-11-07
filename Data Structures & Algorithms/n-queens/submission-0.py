class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDiag, posDiag = set(), set()

        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if c in cols or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                cols.add(c)
                board[r][c] = "Q"
                negDiag.add((r - c))
                posDiag.add((r + c))
                backtrack(r + 1)
                cols.remove(c)
                board[r][c] = "."
                negDiag.remove((r - c))
                posDiag.remove((r + c))

        backtrack(0)
        return res