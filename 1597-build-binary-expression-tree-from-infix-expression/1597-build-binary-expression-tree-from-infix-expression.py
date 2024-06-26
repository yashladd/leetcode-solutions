# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        ops, nums = [], []

        def mock_compute():
            op = ops.pop()
            r = nums.pop()
            l = nums.pop()
            nums.append(Node(val=op, left=l, right=r))

        for ch in s:
            if ch.isdigit():
                nums.append(Node(val=ch))
            elif ch in ['+', '-']:
                while ops and ops[-1] in ['+', '-', '*', '/']:
                    mock_compute()
                ops.append(ch)
            elif ch in ['*', '/']:
                while ops and ops[-1] in ['*', '/']:
                    mock_compute()
                ops.append(ch)
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops[-1] != '(':
                    mock_compute()
                ops.pop()
        while ops:
            mock_compute()
        return nums[0]
        