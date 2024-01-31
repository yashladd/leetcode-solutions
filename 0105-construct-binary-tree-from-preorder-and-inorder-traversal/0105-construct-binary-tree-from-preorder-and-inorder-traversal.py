# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inoMap = {val:i for i, val in enumerate(inorder)}

        p = 0
        def rec(l, r):
            nonlocal p
            if l > r:
                return None

            val = preorder[p]
            root = TreeNode(val)
            p += 1
            idx = inoMap[val]
            root.left = rec(l, idx-1)
            root.right = rec(idx+1, r, )

            return root

        return rec(0, len(inorder)-1)
        