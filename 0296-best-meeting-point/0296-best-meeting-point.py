class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        0  0  0  0  1

        0  1  0  0  0 
         
        0  0  0  0  0

        0  1  0  0  0


        """
        xs = []
        ys = []
        N, M = len(grid), len(grid[0])
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    xs.append(i)
                    ys.append(j)

        xs.sort()
        ys.sort()

        xM, yM = xs[len(xs)//2], ys[len(ys)//2]

        res = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    res += abs(xM - i)
                    res += abs(yM - j)

        return res

        