# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        isP = False
        isQ = False

        def lca(node, p, q):
            nonlocal isP, isQ
            if not node:
                return node

            l = lca(node.left, p, q)
            r = lca(node.right, p, q)

            if node == p or node == q:
                if node == p:
                    isP = True
                if node == q:
                    isQ = True
                return node

            
            if l and r:
                return node

            return l or r

        ans = lca(root, p, q)
        print(ans.val)
        return ans if isP and isQ else None
            