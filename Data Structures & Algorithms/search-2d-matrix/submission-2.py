class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        
        while t <= b:
            p = (t + b) // 2
            if target < matrix[p][0]:
                b = p - 1
            elif matrix[p][-1] < target:
                t = p + 1
            else:
                break


        l, r = 0 , len(matrix[0]) - 1

        while l <= r:

            pivot = ( l + r )// 2
            
            if matrix[p][pivot] == target:
                return True

            elif matrix[p][pivot] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return False