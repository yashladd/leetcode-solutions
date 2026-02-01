from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth_node(group_prev, k)
            if not kth:
                break

            group_next = kth.next  # node right after the k-group

            # Reverse the group: [group_prev.next ... kth]
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # After reversal:
            # prev == kth (new head of this group)
            # group_prev.next was old head, now it's the tail
            old_group_head = group_prev.next
            group_prev.next = kth
            group_prev = old_group_head  # move to tail for next group

        return dummy.next

    def _get_kth_node(self, start: ListNode, k: int) -> Optional[ListNode]:
        curr = start
        for _ in range(k):
            curr = curr.next
            if not curr:
                return None
        return curr
