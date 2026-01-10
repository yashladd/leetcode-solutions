class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # Base Case: Empty tree has size 0
        if not root:
            return 0
        
        # Step 1: Check if the tree rooted at the current 'root' is a BST
        if self.isValidBST(root, float('-inf'), float('inf')):
            # Step 2: If yes, count total nodes in this subtree
            return self.countNodes(root)
        
        # Step 3: If not a BST, recursively find the largest BST in left and right children
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    # Helper 1: Validate BST Property
    def isValidBST(self, node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        # Recursively check left and right with updated ranges
        return self.isValidBST(node.left, min_val, node.val) and \
               self.isValidBST(node.right, node.val, max_val)

    # Helper 2: Count Nodes
    def countNodes(self, node):
        if not node:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)