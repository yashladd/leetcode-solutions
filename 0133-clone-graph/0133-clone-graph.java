/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    Map<Node, Node> cloneMap;

    Node cloneHelper(Node node, Map<Node, Node> cloneMap) {
        if (cloneMap.containsKey(node)){
            return cloneMap.get(node);
        }

        Node copy = new Node(node.val);
        cloneMap.put(node, copy);
        for (Node nei: node.neighbors) {
            copy.neighbors.add(cloneHelper(nei, cloneMap));
        }

        return copy;
    }

    public Node cloneGraph(Node node) {
        if (node == null) return node;
        cloneMap = new HashMap<>();
        return cloneHelper(node, cloneMap);

    }
}