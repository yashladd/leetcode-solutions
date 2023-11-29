"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        h = {}
        
        def f(n):
            if n in h:
                return h[n]
            
            copy = Node(n.val)
            h[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(f(nei))
                
            return copy
        
        return f(node)
        