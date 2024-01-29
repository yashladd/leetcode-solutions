# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        node = root
        if not node:
            return TreeNode(val)
        
        while node:
            # print(node.val)
            isSmaller = node.val > val
            if isSmaller and not node.left:
                node.left = TreeNode(val)
                return root
            elif isSmaller and node.left:
                node = node.left
            elif not isSmaller and not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
                
                
                
            
            
        