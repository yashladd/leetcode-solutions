"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        
        def areSame(r1, r2, c1, c2):
            val = grid[r1][c1]
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] != val:
                        return -1 , False
            return val, True
                    
        def f(r1, r2, c1, c2):
            val, same = areSame(r1, r2,c1, c2)
            if same:
                return Node(val, same, None, None, None, None)
            
            midR, midC = (r1 + r2) // 2, (c1 + c2) // 2
            
            topLeft = f(r1,midR, c1, midC)
            bottomLeft = f(midR, r2, c1, midC)
            topRight = f(r1, midR, midC, c2)
            bottomRight = f(midR, r2, midC, c2)
            
            root = Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
            
            
            return root
        
        return f(0, n, 0, n)
            
        