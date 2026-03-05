class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        

        n, m = len(mat), len(mat[0])

        prev = list(map(int, mat[0]))
        maxi = max(prev)
        for row in range(1, n):
            curr =  [0] * m

            for col in range(m):
                if mat[row][col] == "1":
                    curr[col] = 1 + min(
                        prev[col],
                        prev[col-1] if col - 1 >= 0 else 0,
                        curr[col-1] if col-1 >= 0 else 0 
                    )
                    maxi = max(maxi, curr[col])                
            prev = curr

        return maxi * maxi