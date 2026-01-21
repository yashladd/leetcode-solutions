# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        s = f =  head
        found = False
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                found = True
                break 
                
        if not found:
            return None
        
        s = head
        
        while s!=f:
            s = s.next
            f = f.next
            
        return s
                
        
        