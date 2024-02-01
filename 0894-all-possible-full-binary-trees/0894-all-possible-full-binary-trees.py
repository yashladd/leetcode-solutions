# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def f(x):
            if x % 2 == 0:
                return []
            if x == 1:
                return [TreeNode()]
            
            res = []
            for i in range(1, x, 2):
                for left in f(i):
                    for right in f(x-i-1):
                        root = TreeNode(0, left, right)
                        res.append(root)
                        
            return res
        
        
        return f(n)
        