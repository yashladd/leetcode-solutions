# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = f = head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            
        h2 = s.next
        s.next = None
        
        p, c = None, h2
        while c:
            nex = c.next
            c.next = p
            p = c
            c = nex
            
        h2 = p
        h1 = head
        dummy = ListNode(-1)
        tail = dummy
        while h1 or h2:
            tail.next = h1
            tail = h1
            h1 = h1.next
            if h2:
                tail.next = h2
                tail = h2
                h2 = h2.next
        # return dummy.next
            
        
        