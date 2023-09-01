# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getLeftH(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def getRightH(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
                
        def f(node):
            if not node:
                return 0
            lh = getLeftH(node)
            rh = getRightH(node)

            if lh == rh:
                return (2**lh - 1)
            else:
                return 1 + f(node.left) + f(node.right)
                
        return f(root)
        