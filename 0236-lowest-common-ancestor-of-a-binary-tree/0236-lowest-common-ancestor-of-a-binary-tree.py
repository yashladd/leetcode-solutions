# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node):
            if not node: return None

            left = lca(node.left)
            right = lca(node.right)

            if node.val in [p.val, q.val]:
                return node

            if left and right:
                return node
            
            return left or right

        return lca(root)

            

        