import java.util.Stack;

class Solution {
    
    // Common function to push linked list values onto a stack
    private void fillStack(Stack<Integer> s, ListNode n) {
        while (n != null) {
            s.push(n.val);
            n = n.next;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();

        // 1. Use the helper function to fill both stacks
        fillStack(s1, l1);
        fillStack(s2, l2);

        int sum = 0;
        ListNode head = null;

        // 2. Standard addition logic using the stacks
        while (!s1.isEmpty() || !s2.isEmpty() || sum > 0) {
            if (!s1.isEmpty()) {
                sum += s1.pop();
            }
            if (!s2.isEmpty()) {
                sum += s2.pop();
            }

            // Create new node for the current digit
            ListNode n = new ListNode(sum % 10);
            
            // Insert at the front (Head)
            n.next = head;
            head = n;

            // Update carry
            sum /= 10;
        }

        return head;
    }
}