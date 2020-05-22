class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        res += 1
                    else:
                        updated = min(matrix[row-1][col-1], matrix[row][col-1], matrix[row-1][col]) + matrix[row][col]
                        res += updated
                        matrix[row][col] = updated
        return res
        
        
