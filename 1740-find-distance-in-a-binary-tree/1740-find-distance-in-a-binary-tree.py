# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def get_path_reverse(node, target, path):
            if not node:
                return False
                
            # 1. Base Case: We found the target! Append it first.
            if node.val == target:
                path.append(node.val)
                return True
                
            # 2. Recurse left and right
            left_found = get_path_reverse(node.left, target, path)
            right_found = get_path_reverse(node.right, target, path)
            
            # 3. If the target was found below us, append this current node
            if left_found or right_found:
                path.append(node.val)
                return True
                
            return False

        path_p = []
        path_q = []
        
        get_path_reverse(root, p, path_p)
        get_path_reverse(root, q, path_q)
        
        # Both paths now end with the root. 
        # We pop from the end as long as the elements match.
        while path_p and path_q and path_p[-1] == path_q[-1]:
            path_p.pop()
            path_q.pop()
            
        # The remaining elements in both arrays are the unshared nodes!
        return len(path_p) + len(path_q)