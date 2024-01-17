# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        from heapq import heappush, heappop
        #NOTE: Python doesn't allow inserting objects which are not comparable as second value
        # Since second object in the tuple must be a comparable, you can either insrert: 
        # 1: (node.val, i, node)
        # 2: (node.val, i)
        for i in range(len(lists)):
            if lists[i]:
                heappush(q, (lists[i].val, i))
        dummy = ListNode(-1)
        curr = dummy
        while q:
            _, i = heappop(q)
            curr.next = lists[i]
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(q, (lists[i].val, i))
                
        return dummy.next
            
                    
        
        