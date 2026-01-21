# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Proof they are at same distance


        x = distance before entering loop 
        y = distance from loop to pt where they meet
        z = distance from pt to start of loop 

        l = length of the loop = z + y

        distance traveleed by fast = 
        f = x + p*l + y
        s = x + q*l + y

        2s = f

        2x + 2ql + 2y = x + pl + y

        x + y = k*l
        y = l - z from above

        x = k*l + z



        """
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
                
        
        