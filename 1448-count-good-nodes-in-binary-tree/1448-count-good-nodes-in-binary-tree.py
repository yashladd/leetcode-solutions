# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def f(root, path):
            nonlocal cnt
            if root:
                if all([p <= root.val for p in path]):
                    cnt += 1
                    
                f(root.left, path + [root.val])
                f(root.right, path + [root.val])
                
        f(root, [])
        return cnt
                
        