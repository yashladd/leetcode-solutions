# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None
        # curr = root
        # while curr:
        #     if curr.val > p.val:
        #         succ = curr
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        # return succ
        def f(node, p):
            nonlocal succ
            if node:
                if node.val > p.val:
                    succ = node
                    f(node.left, p)
                else:
                    f(node.right, p)
        f(root, p)
        return succ

        