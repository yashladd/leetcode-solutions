# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delHelper(self, node, forests):
        if not node:
            return None

        node.left = self.delHelper(node.left, forests)
        node.right = self.delHelper(node.right, forests)
        if node.val in self.to_del:
            if node.left: forests.add(node.left)
            if node.right: forests.add(node.right)
            forests.discard(node)
            return None

        return node
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_del = set(to_delete)

        forests = set()

        self.delHelper(root, forests)

        if root.val not in self.to_del:
            forests.add(root)

        return list(forests)