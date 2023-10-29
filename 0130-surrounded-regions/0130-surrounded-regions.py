class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        if not n: return 
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m \
                or board[i][j] != "O":
                return 
            
            board[i][j] = "T"
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                x, y = i + dx, j + dy
                dfs(x, y)
                
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
            
        for j in range(1, m):
            dfs(0, j)
            dfs(n-1, j)
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        