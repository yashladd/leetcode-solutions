# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delHelper(self, node, forests, is_root):
        if not node:
            return None

        should_del = node.val in self.to_del

        if not should_del and is_root:
            forests.append(node)

        node.left = self.delHelper(node.left, forests, should_del)
        node.right = self.delHelper(node.right, forests, should_del)

        return None if should_del else node

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_del = set(to_delete)
        forests = []

        self.delHelper(root, forests, True)

        return forests