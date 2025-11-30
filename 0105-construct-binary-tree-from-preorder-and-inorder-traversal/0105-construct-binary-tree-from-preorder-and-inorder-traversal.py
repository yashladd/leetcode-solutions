# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h = { nodeVal: i for i, nodeVal in enumerate(inorder)}


        def b(p, l, r):
            # print(p, ino)
            if l > r :
                return None
                # or not p
            val = p.popleft()
            root = TreeNode(val)

            # print(root, type(root))
            # print(root.val, p, ino)
            idx = h[val]
            le = b(p, l, idx-1)
            ri = b(p, idx+1, r)

            root.left = le
            root.right = ri
            return root

        return b(deque(preorder), 0, len(inorder)-1)

        