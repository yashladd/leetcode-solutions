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
        dummy = Node(-1)
        h = {}
        h[None] = None
        tail = dummy
        curr = head
        while curr:
            copy = Node(curr.val)
            h[curr] = copy
            tail.next = copy
            tail = copy
            curr = curr.next
            
        curr = head
        while curr:
            rand = h[curr.random]
            h[curr].random = rand
            curr = curr.next
            
        return dummy.next