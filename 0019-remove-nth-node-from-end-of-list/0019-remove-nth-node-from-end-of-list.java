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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        int l = 0;
        ListNode c = head;
        ListNode d = new ListNode(-1, head);
        while (c != null) {
            l++;
            c = c.next;
        }

        ListNode p = d;
        c = head;
        int steps = l - n + 1;
        while (--steps > 0) {
            ListNode nex = c.next;
            p = c;
            c = nex;
        }

        p.next = p.next.next;

        return d.next;
        
    }
}