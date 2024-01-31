# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        m = {v:i for i, v in enumerate(inorder)}
        
        def rec(l, r):
            if l > r:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            idx = m[val]
            root.right = rec(idx+1, r)
            root.left = rec(l, idx-1)
            
            return root
        
        return rec(0, len(inorder)-1)
        