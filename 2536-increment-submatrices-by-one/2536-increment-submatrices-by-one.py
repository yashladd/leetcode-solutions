class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        incs = [[0 for _ in range(n)] for _ in range(n)]

        for tr, tc, br, bc in queries:
            for row in range(tr, br+1):
                incs[row][tc] += 1
                if (1 + bc) < n:
                    incs[row][1+bc] -= 1

        for i in range(n):
            for j in range(1,n):
                incs[i][j] += incs[i][j-1] 

        return incs

        