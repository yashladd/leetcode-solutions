# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def f(r, s):
            if r:
                if r.val == s.val:
                    if same(r, s):
                        return True
                l = f(r.left, s)
                if l: return True
                r = f(r.right, s)
                if r: return True
            
            return False
        
        def same(p, q):
            if not p or not q:
                return p == q
            return p.val == q.val and same(p.left, q.left) and same(p.right , q.right)
        
        
        return f(root, subRoot)