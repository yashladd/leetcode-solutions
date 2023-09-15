# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return None
        
        def frmost(node):
            curr = node
            while curr and curr.right:
                curr = curr.right
            return curr
            
        def rearrange(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            rch = node.right
            rmost = frmost(node.left)
            rmost.right = rch
            return node.left
            
        
        if root.val == key:
            return rearrange(root)
            
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = rearrange(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = rearrange(curr.right)
                    break
                else:
                    curr = curr.right
                    
        return root
            
            
        