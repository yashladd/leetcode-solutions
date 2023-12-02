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
        s, f = head, head
        
        while f.next and f.next.next:
            s, f = s.next, f.next.next
        
        curr = s.next
        s.next = None
        
        prev= None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        p1 = head
        p2 = prev
        d = ListNode(-1, p1)
        # tail = d
        while p1 and p2:
            n1 = p1.next
            n2 = p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
            
        return d.next
            
            
            
            