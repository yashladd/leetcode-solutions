# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2: return l1 or l2
        nh = l1 if l1.val <= l2.val else l2
        dummy = ListNode(-1, nh)
        p1, p2 = l1, l2
        tail = dummy
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
                
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
            
        return dummy.next
                
            
        