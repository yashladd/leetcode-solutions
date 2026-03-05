class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            
            # Check if this node itself needs to be deleted
            deleted = node.val in to_del
            
            # If this node is a root and not deleted, add to result
            if is_root and not deleted:
                forest.append(node)
            
            # Recurse: if this node is deleted, its children become potential roots
            node.left = helper(node.left, deleted)
            node.right = helper(node.right, deleted)
            
            return None if deleted else node

        helper(root, True)
        return forest