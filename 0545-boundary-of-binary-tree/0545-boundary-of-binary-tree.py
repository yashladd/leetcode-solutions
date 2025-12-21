# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = [root.val]
        
        if self.is_leaf(root):
            return result
        
        self.add_left_boundary(root.left, result)
        
        self.add_leaves(root, result)
        
        self.add_right_boundary(root.right, result)
        
        return result

    # --- Helper Methods ---

    def is_leaf(self, node: Optional[TreeNode]) -> bool:
        return node and not node.left and not node.right

    def add_left_boundary(self, node: Optional[TreeNode], result: List[int]):
        # Stop if null or if it's a leaf (leaves are handled separately)
        if not node or self.is_leaf(node):
            return
        
        result.append(node.val)
        
        # Prioritize left child; if missing, go right
        if node.left:
            self.add_left_boundary(node.left, result)
        else:
            self.add_left_boundary(node.right, result)

    def add_leaves(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return
        
        if self.is_leaf(node):
            result.append(node.val)
            return
        
        self.add_leaves(node.left, result)
        self.add_leaves(node.right, result)

    def add_right_boundary(self, node: Optional[TreeNode], result: List[int]):
        if not node or self.is_leaf(node):
            return
        
        # Prioritize right child; if missing, go left
        if node.right:
            self.add_right_boundary(node.right, result)
        else:
            self.add_right_boundary(node.left, result)
        
        # Append AFTER the recursion calls to get reverse order (bottom-up)
        result.append(node.val)