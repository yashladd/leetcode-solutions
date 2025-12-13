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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode c = head;
        for (int i = 0; i < k; i++) {
            if (c == null){
                return head;
            }
            c = c.next;
        }
        
        ListNode p = null;
        c = head;
        for (int i = 0; i < k; i++) {
            ListNode n = c.next;
            c.next = p;
            p = c;
            c = n;
        }

        head.next = reverseKGroup(c, k);
        return p;

    }
}