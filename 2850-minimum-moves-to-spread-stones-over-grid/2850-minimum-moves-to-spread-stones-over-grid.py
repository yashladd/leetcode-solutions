class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeros = []
        extra = []
        for i in range(3):
            for j in range(3):
                if not grid[i][j]:
                    zeros.append((i,j))
                elif grid[i][j] > 1:
                    extra.append([i, j, grid[i][j]-1])
        self.mini = 100

        if not zeros:
            return 0

        
        def f(i, cnt):
            if i >= len(zeros):
                self.mini = min(self.mini, cnt)
                return 

            for j in range(len(extra)):
                if not extra[j][2]:
                    continue

                extra[j][2] -= 1

                f(i+1, abs(extra[j][0] - zeros[i][0]) + abs(extra[j][1] - zeros[i][1]) + cnt)

                extra[j][2] += 1

        f(0, 0)

        return self.mini
