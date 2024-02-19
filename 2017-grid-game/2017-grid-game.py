class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = 2
        m = len(grid[0])
        choices = [[0] * m for _ in range(2) ]
        post = 0
        for col in range(m-1, 0, -1):
            post = post + grid[0][col]
            choices[0][col] = post
        pre = 0
        for col in range(0, m-1):
            pre += grid[1][col]
            choices[1][col] = pre
        best = float("inf")
        for i in range(m):
            rightSum, leftSum = 0, 0
            if i >= 1:
                leftSum = choices[1][i-1]
            if i <= m-2:
                rightSum = choices[0][i+1]
            best = min(best, max(rightSum, leftSum))
        return best


        