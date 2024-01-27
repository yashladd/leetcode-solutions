class Solution:
    def longestIncreasingPath(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        
        def inb(i, j):
            return i >= 0 and j >= 0 and i < n and j < m
        
        @cache
        def dfs(i, j):
            path = 1
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i + dx, j + dy
                if inb(r,c) and g[r][c] > g[i][j]:
                    path = max(path, 1 + dfs(r, c))
                    
            return path
        
        return max(dfs(i,j) for i, j in product(range(n), range(m)))
        
        
        