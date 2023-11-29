class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p, a = set(), set()
        def dfs(i, j, v, ph):
            if i < 0 or j < 0 or i >= m or j >= n or (i,j) in v or heights[i][j] < ph:
                return 
            
            v.add((i,j))
            dfs(i-1, j, v, heights[i][j])
            dfs(i, j-1, v, heights[i][j])            
            dfs(i+1, j, v, heights[i][j])            
            dfs(i, j+1, v, heights[i][j])
            
        for c in range(n):
            dfs(0, c, p, heights[0][c])
            dfs(m-1, c, a, heights[m-1][c])  
            
        for r in range(m):
            dfs(r, 0, p, heights[r][0])
            dfs(r, n-1, a, heights[r][n-1])        
            
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in p and (i,j) in a:
                    res.append((i,j))
                    
        return res
            