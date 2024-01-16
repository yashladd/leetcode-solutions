"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        def copy():
            c = head
            while c:
                nex = c.next
                node = Node(c.val)
                c.next = node
                node.next = nex
                c = nex
                
        def random():
            c = head
            while c:
                if c.random:
                    c.next.random = c.random.next
                c = c.next.next
        
        def remove():
            dummy = Node(-1, head.next)
            tail = dummy
            curr = head
            while curr:
                tail.next = curr.next
                tail = tail.next
                curr.next = tail.next
                curr = curr.next
            return dummy.next
        
        copy()
        random()
        return remove()
        