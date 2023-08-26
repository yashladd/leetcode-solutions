# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ino = [] 
        curr = root
        while curr:
            if not curr.left:
                ino.append(curr.val)
                curr = curr.right
            else:
                conn = curr.left
                while conn.right and conn.right != curr:
                    conn = conn.right
                
                if not conn.right:
                    conn.right = curr
                    curr = curr.left
                else:
                    conn.right = None
                    ino.append(curr.val)
                    curr = curr.right
                    
        return ino
                