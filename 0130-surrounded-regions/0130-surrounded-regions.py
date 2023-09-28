class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        # n, m = len(board), len(board[0])
#         vis = [[0 for _ in range(m)] for _ in range(n)]

#         def inb(i, j):
#             return i >= 0 and j >= 0 and i < n and j < m
#         def dfs(i, j):
#             vis[i][j] = 1
#             for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 r, c = i + dx, j + dy
#                 if inb(r, c) and board[r][c] == "O" and not vis[r][c]:
#                     dfs(r, c)

#         for c in range(m):
#             if not vis[0][c] and board[0][c] == "O":
#                 dfs(0, c)
#             if not vis[n-1][c] and board[n-1][c] == "O":
#                 dfs(n-1, c)

#         for r in range(1, n-1):
#             if not vis[r][0] and board[r][0] == "O":
#                 dfs(r, 0)
#             if not vis[r][m-1] and board[r][m-1] == "O":
#                 dfs(r, m-1)

#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == "O" and not vis[i][j]:
#                     board[i][j] = "X" 
