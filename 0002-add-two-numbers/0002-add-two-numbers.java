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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p = l1, q = l2;
        int c = 0;

        ListNode d = new ListNode(-1), t = d;

        while (p != null || q!=null || c > 0 ) {
            int pval = p != null ? p.val : 0;
            int qval = q != null ? q.val : 0;

            int sum = pval + qval + c;
            ListNode n = new ListNode(sum % 10);
            t.next = n;
            t = n;
            c =  (int) sum / 10;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        } 

        if (c > 0) {
            t.next = new ListNode(1);
        }

        return d.next;
    }
}