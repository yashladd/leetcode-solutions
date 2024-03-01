# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s=f=head
        while f.next and f.next.next:
            s, f = s.next, f.next.next

        cur = s.next
        s.next = None

        p = nex = None
        while cur:
            nex = cur.next
            cur.next = p
            p = cur
            cur = nex
        maxi = 0
        q= head
        while p and q:
            maxi = max(p.val + q.val, maxi)
            p = p.next
            q = q.next
        return maxi
        