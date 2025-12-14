/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        Map<Node, Node> mp = new HashMap<>();
        mp.put(null, null);

        Node c = head, d = new Node(-1), t = d;
        while (c != null) {
            mp.put(c, new Node(c.val));
            c = c.next;
        }

        c = head;

        while (c != null) {
            t.next = mp.get(c);
            t = t.next;
            t.random = mp.get(c.random);
            c = c.next;
        }
        return d.next;





        
    }
}