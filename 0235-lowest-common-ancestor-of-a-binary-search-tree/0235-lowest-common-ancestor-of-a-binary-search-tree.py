# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def f(r, p, q):
            if r:
                if r.val < p.val and r.val < q.val:
                    return f(r.right, p, q)
                elif r.val > p.val and r.val > q.val:
                    return f(r.left, p, q)
                else:
                    return r
            
        return f(root, p, q)
        