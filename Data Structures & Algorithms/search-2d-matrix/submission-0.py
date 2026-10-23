class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) -1:
            if matrix[row + 1][0] == target:
                return True
            if matrix[row + 1][0] < target:
                row += 1
            else:
                break


        l, r = 0 , len(matrix[0]) - 1

        while l <= r:

            pivot = ( l + r )// 2
            
            if matrix[row][pivot] == target:
                return True

            elif matrix[row][pivot] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return False