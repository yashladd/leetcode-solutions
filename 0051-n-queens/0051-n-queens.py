class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [["."] * n for i in range(n) ]    
        res = []
        def rec(row):
            if row == n:
                res.append(["".join(board[i]) for i in range(n)])
                return 

            for col in range(n):
                if col not in cols and (row + col) not in diag1 and row - col not in diag2:
                    cols.add(col)
                    diag1.add(row + col)
                    diag2.add(row-col)
                    board[row][col] = "Q"
                    rec(row+1)
                    cols.remove(col)
                    diag1.remove(row + col)
                    diag2.remove(row-col)
                    board[row][col] = "."

        rec(0)

        return res


        