class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n, m = len(board), len(board[0])
        
        dirs = [[0,1], [1,0], [0,-1], [-1,0],
                [1,1], [1,-1], [-1,-1], [-1,1]]
        
        board[rMove][cMove] = color
        
        def legal(r, c, col, d):
            dx, dy = d
            length = 1
            i, j = r + dx,  c + dy
            
            while i >= 0 and j >= 0 and i < n and j < m:
                length += 1
                if board[i][j] == ".": return False
                if board[i][j] == col:
                    return length >= 3
                i, j = i + dx, j + dy
        
        
        for d in dirs:
            if legal(rMove, cMove, color, d):
                return True
        return False
                
                
        
    