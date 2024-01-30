# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        
        def reorder(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            rightCh = node.right
            rightMost = node.left
            while rightMost.right:
                rightMost = rightMost.right
            rightMost.right = rightCh
            return node.left
            
            
        if root.val == key:
            return reorder(root)
        
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = reorder(curr.left)
                else: curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = reorder(curr.right)
                else:
                    curr = curr.right
        return root
                
                
                
            
        
        
        
        