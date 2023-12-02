# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 or not list2:
            return list1 or list2

        h1, h2 = list1, list2
        head = h1 if h1.val < h2.val else h2
        d = ListNode(-1)
        p = d
        c1, c2 = h1, h2
        while c1 or c2:
            v1 = c1.val if c1 else float("inf")
            v2 = c2.val if c2 else float("inf")
            nex = None
            if v1 < v2:
                if c1.next:
                    nex = c1.next
                p.next = c1
                p = c1
                c1 = nex
            else:
                if c2.next:
                    nex = c2.next
                    
                p.next = c2
                p = c2
                c2 = nex
        return d.next
                
                
        

            
        