# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # 1. Determine the depth (count the dashes)
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
                
            # 2. Extract the node value (handle multi-digit numbers)
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
                
            # 3. Create the new node
            node = TreeNode(val)
            
            # 4. Maintain the stack invariant
            # Pop from stack until the stack size equals the current depth
            while len(stack) > depth:
                stack.pop()
                
            # 5. Attach the node to its parent (the top of the stack)
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                    
            # 6. Push the current node onto the stack as the new active path
            stack.append(node)
            
        # The root is always the first element pushed to the stack
        return stack[0] if stack else None