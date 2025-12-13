# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        s, f = head, head
        while f.next and f.next.next:
            s, f = s.next, f.next.next

        nex = s.next
        s.next = None

        p, c = None, nex
        while c:
            nex = c.next
            c.next = p
            p = c
            c = nex

        while p:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next

        return True
        