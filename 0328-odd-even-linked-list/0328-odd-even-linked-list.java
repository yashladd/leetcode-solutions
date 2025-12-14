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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode even = head.next, odd = head, evenHead = even;

        


        while (even != null && even.next != null) {
            //      t
            //      |            
            // 1 -> 2 -> 3
            // o    e 

            // t -> 2 
            
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = odd.next;
            
        }
        odd.next = evenHead;
        return head;
    }
}