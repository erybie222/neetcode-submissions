class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareSets = [[set() for i in range(len(board[0])//3)] for j in range(len(board)//3)]
        colSets = [set() for i in range(len(board[0]))]
        rowSets = [set() for i in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] not in rowSets[r]:
                        rowSets[r].add(board[r][c])
                    else:
                        return False
                    if board[r][c] not in colSets[c]:
                        colSets[c].add(board[r][c])
                    else:
                        return False
                    if board[r][c] not in squareSets[r//3][c//3]:
                        squareSets[r//3][c//3].add(board[r][c])
                    else:
                        return False
        return True