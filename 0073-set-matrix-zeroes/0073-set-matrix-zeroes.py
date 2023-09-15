class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col_0 = False
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] == 0:
                is_col_0 = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(n-1, -1, -1):
            
            for j in range(m-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if is_col_0:
                matrix[i][0] = 0