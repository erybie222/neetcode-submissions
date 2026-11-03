class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c, count):
            if count == len(word):
                return True
            elif (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[count]):
                return
            visited.add((r, c))
            res = (
                dfs(r + 1, c, count + 1) or
                dfs(r - 1, c, count + 1) or
                dfs(r, c + 1, count + 1) or
                dfs(r, c - 1, count + 1)
                )
            visited.remove((r, c))
            return res

            
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False