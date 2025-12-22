class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        0 -> 0 0
        1 -> 0 1
        0 -> 1 2
        1 -> 1 3
        """
        n, m = len(board), len(board[0])


        def countOneNeighs(r, c):
            nei = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >=n or j >= m:
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei

        for i in range(n):
            for j in range(m):
                neighs = countOneNeighs(i, j)

                if board[i][j]:
                    if neighs in [2, 3]:
                        board[i][j] = 3
                else:
                    if neighs == 3:
                        board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] in [2, 3]:
                    board[i][j] = 1
                elif board[i][j] == 1:
                    board[i][j] = 0
        
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     0 -> 0 0
    #     1 -> 0 1
    #     0 -> 1 2
    #     1 -> 1 3



    #     """
        