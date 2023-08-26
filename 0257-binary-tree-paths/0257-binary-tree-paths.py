# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def f(root, ds):
            if not root.right and not root.left:
                a = ds + [root.val]
                res.append(a.copy())
                return 

            if root:
                if root.left:
                    f(root.left, ds + [root.val])
                if root.right:
                    f(root.right, ds + [root.val])
        
        f(root, [])
        ans = ["->".join(list(map(lambda x: str(x), a))) for a in res]
        return ans
        