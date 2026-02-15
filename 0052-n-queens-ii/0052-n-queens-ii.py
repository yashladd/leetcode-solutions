class Solution:
    def totalNQueens(self, n: int) -> int:
        """
          0  1  2   3 
        0 0 -1 -2   -3
        1 1  0  -1  -2
        2 2  1  0   -1
        3 3  2  1   0
        
        """
        rows = set()
        cols = set()
        diag = set()
        anti = set()
        
        cnt = 0
        board = [["." for _ in range(n)] for _ in range(n)]
        def f(row):
            if row == n:
                return 1
            
            ways = 0
            
            for col in range(n):
                if board[row][col] == "." and row not in rows and col not in cols and row + col not in diag and row - col not in anti:
                    cols.add(col)
                    rows.add(row)
                    diag.add(row + col)
                    anti.add(row-col)
                    
                    board[row][col] == "!"
                    
                    ways += f(row + 1)
                    
                    board[row][col] == "."
                    rows.discard(row)
                    cols.discard(col)
                    diag.discard(row + col)
                    anti.discard(row - col)
                    
            return ways
                    
                    
                    
        
        return f(0)
            