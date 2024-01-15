# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2, c = l1, l2, 0
        dummy = ListNode(-1)
        tail = dummy
        while c1 or c2 or c:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            tot = v1 + v2 + c
            node = ListNode(tot%10)
            c = tot//10
            tail.next = node
            tail = node
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
                
        return dummy.next
            
        