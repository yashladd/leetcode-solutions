class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.a = [[0] * (m + 1) for _ in range(n+1)]
        """
           0   1   2   3   4   5
        
        0  0   0   0   0   0   0
        1  0   3   3   4   8  10
        2  0   8  14  18  24  27
        3  0   9  17  21  28  36
        4  0  13  22  26  34  49
        5  0  14  23  30  38  58
        """

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.a[i][j] = (
                    matrix[i-1][j-1] +
                    self.a[i-1][j] +
                    self.a[i][j-1] -
                    self.a[i-1][j-1]
                )

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (
            self.a[row2+1][col2+1] -
            self.a[row1][col2+1] - 
            self.a[row2+1][col1] +
            self.a[row1][col1]
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)