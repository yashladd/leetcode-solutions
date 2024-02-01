# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], L: int, R: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val >= L and root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        
        # All right children can be deleted
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # root.val < L: all left children can be deleted
        return self.trimBST(root.right, L, R)
        