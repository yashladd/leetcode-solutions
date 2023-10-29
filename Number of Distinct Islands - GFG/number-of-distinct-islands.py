#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        
        s = set()
        def inb(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            return True
            
        def dfs(i, j, curr, origin):
            
            
            ox, oy = origin
            curr.append((i - ox, j - oy))
            vis[i][j] = 1
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i + dx, j + dy
                if inb(r, c) and not vis[r][c] and grid[r][c]:
                    dfs(r, c, curr, origin)
                    
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    c = []
                    dfs(i, j, c, (i, j))
                    s.add(tuple(c))
                    
        return len(s)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends