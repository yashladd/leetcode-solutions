class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        
        # States:
        # 0: Uncovered (Needs Camera)
        # 1: Has Camera
        # 2: Covered (No Camera needed)
        
        def dfs(node):
            if not node:
                return 2  # Null nodes are "covered"
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If any child is uncovered, we MUST place a camera here
            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            
            # If any child has a camera, this node is covered
            if left == 1 or right == 1:
                return 2
            
            # If both children are covered (but have no cameras to help us),
            # this node becomes uncovered.
            return 0
            
        # Run DFS
        root_state = dfs(root)
        
        # Edge Case: If the root itself returns "Uncovered", we need one last camera for it
        if root_state == 0:
            self.cameras += 1
            
        return self.cameras