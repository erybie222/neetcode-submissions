class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                elif val in rows[i]:
                    return False
                elif val in cols[j]:
                    return False
                elif val in boxes[i//3 *3 + j//3]:
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[i//3 *3 + j//3].add(val)
        return True