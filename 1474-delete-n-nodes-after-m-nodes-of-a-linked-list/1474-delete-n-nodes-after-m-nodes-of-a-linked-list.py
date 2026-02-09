# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        
        
        p, c = dummy, head
        """
        #[ d 1,2,3,4,5,6,7,8,9,10,11,12,13]
             p c
           k = 1
        """        
        while c:
            keep, delete = 1, 1
            while keep <= m and c:
                p = c
                c = c.next
                keep += 1
            if not c:
                return dummy.next
            
            while delete <= n and c:
                p.next= c.next
                c.next = None
                c = p.next
                delete += 1
                
        
        return dummy.next
            
            
            
            
                
                
                