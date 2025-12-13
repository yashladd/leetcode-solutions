/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode p = list1, q = list2;

        ListNode dummy = new ListNode(-1);

        ListNode tail = dummy;

        while (p != null || q != null) {
            int pval = p != null ? p.val : Integer.MAX_VALUE;
            int qval = q != null ? q.val : Integer.MAX_VALUE;

            if (pval <= qval) {
                ListNode nex = p.next;
                tail.next = p;
                tail = tail.next;
                tail.next = null;
                p = nex;
            } else {
                ListNode nex = q.next;
                tail.next = q;
                tail = tail.next;
                tail.next = null;
                q = nex;
            }
        }

        return dummy.next;

        
    }
}