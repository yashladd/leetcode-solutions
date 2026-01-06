# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        d  = ListNode(-1)

        # print(type(lists[0]))
        t = d

        h = []

        for i, l in enumerate(lists):
            if l:
                heappush(h, (l.val, i))

        while h:
            val, idx = heappop(h)
            t.next = lists[idx]
            nex = lists[idx].next
            lists[idx] = nex
            t = t.next
            t.next = None
            if nex:
                heappush(h, (nex.val, idx))


        return d.next