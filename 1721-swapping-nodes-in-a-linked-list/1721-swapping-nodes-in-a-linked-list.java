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
    public ListNode swapNodes(ListNode head, int k) {

        ListNode c = head, kThBackNode = head, kthFrontNode;
        int len = 0; 
        for (int i = 0; i < k-1; i++) {
            c = c.next;
        }

        kthFrontNode = c;
        
        while (c != null && c.next != null) {
            kThBackNode = kThBackNode.next;
            c = c.next;
        }

        int endNodeVal = kThBackNode.val;
        int frontNodeVal = kthFrontNode.val;
        kThBackNode.val = frontNodeVal;
        kthFrontNode.val = endNodeVal;


        return head;        
    }
}