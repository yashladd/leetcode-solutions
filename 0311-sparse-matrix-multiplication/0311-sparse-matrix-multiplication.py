class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k =len(mat1), len(mat1[0])
        k, n = len(mat2), len(mat2[0])
        res = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize res with zeros first
        for i in range(m):
            for p in range(k):
                if mat1[i][p] != 0:  # Optimization: Skip zeros
                    for j in range(n):
                        res[i][j] += mat1[i][p] * mat2[p][j]

        return res
        