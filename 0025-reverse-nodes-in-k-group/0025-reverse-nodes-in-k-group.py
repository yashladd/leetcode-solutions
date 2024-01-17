# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # BASE CASE
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next
            
        prev, curr = None, head
        for i in range(k):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        head.next = self.reverseKGroup(curr, k)
        return prev
        