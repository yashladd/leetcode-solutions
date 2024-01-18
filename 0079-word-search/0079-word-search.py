class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        r, c = len(board), len(board[0])
        def inb(i, j):
            return i < r and i >= 0 and j < c and j >= 0
        vis = [[0] * c for _ in range(r)] 
        
        def dfs(i, j, match, vis):
            vis[i][j] = 1
            if match == n-1:
                return board[i][j] == word[match]
            
            if board[i][j] == word[match]:
                for dx, dy in [[0, 1], [1,0], [0,-1], [-1, 0]]:
                    x, y = i + dx, j + dy
                    if inb(x, y) and not vis[x][y]:
                        if dfs(x, y, match + 1, vis):
                            return True

            vis[i][j] = 0
            return False
        
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, vis):
                        return True
                    
        return False
        