# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def reorder(self, root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        rCh = root.right
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = rCh
        return root.left
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val < low or root.val > high:
            root =  self.reorder(root)
            if not root:
                return root
            else:
                return self.trimBST(root, low, high)
        
        if root.left and (root.left.val < low or root.left.val > high):
            root.left = self.reorder(root.left)
            # if root.left:
            #     root.left = self.trimBST(root.left, low, high)
            
        if root.right and (root.right.val < low or root.right.val > high):
            root.right = self.reorder(root.right)
            # if root.right:
            #     root.right = self.trimBST(root.right, low, high)
            
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
            
        return root
            
        