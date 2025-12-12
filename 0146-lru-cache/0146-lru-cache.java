import java.util.HashMap;
import java.util.Map;

class LRUCache {

    // --- Inner Node Class for Doubly-Linked List ---
    class Node {
        int key;    // Must store the key to remove the entry from the HashMap upon eviction
        int val;
        Node prev;
        Node next;

        // Constructor for actual data nodes
        Node(int key, int val) {
            this.key = key;
            this.val = val;
        }

        // Constructor for dummy head/tail nodes (val is ignored)
        Node(int val) {
            this.val = val;
        }
    }

    // --- LRUCache Fields (Instance Variables) ---
    private final int capacity;
    // Maps the key to its corresponding Node in the linked list for O(1) lookups
    private final Map<Integer, Node> cache; 
    
    // Dummy head and tail nodes to simplify list operations (head.next is MRU, tail.prev is LRU)
    private final Node head;
    private final Node tail;

    // --- Constructor ---
    public LRUCache(int capacity) {
        // Fix 1: Initialize fields in the class, not in the constructor with 'static'.
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        this.head = new Node(-1);
        this.tail = new Node(-1);
        
        // Link head and tail initially
        head.next = tail;
        tail.prev = head;
    }

    // --- Helper Methods for Doubly-Linked List (O(1)) ---
    
    /**
     * Removes a given node from the list.
     */
    private void removeNode(Node n) {
        // Fix 2: The implementation you had for removeNode looked correct conceptually,
        // but it needs to be an instance method.
        n.prev.next = n.next;
        n.next.prev = n.prev;
        // Optionally clear references for Garbage Collection, though not strictly required
        n.prev = null;
        n.next = null;
    }

    /**
     * Adds a given node right after the head (making it the MRU).
     */
    private void addFront(Node n) {
        Node currentMRU = head.next;
        
        // 1. Link new node 'n'
        n.next = currentMRU;
        n.prev = head;
        
        // 2. Link surrounding nodes to 'n'
        head.next = n;
        currentMRU.prev = n;
    }

    // --- Main Methods ---

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }

        Node node = cache.get(key);
        
        // Update Recency: move node to the front (MRU)
        removeNode(node);
        addFront(node);
        
        return node.val;
    }

    public void put(int key, int value) {
        // 1. Update Case
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.val = value; // Update the value
            
            // Update Recency: move node to the front (MRU)
            removeNode(node);
            addFront(node);
            return;
        }

        // 2. New Insertion Case (Check Capacity)
        if (cache.size() == capacity) {
            // Evict LRU item (the node just before the dummy tail)
            Node lruNode = tail.prev;
            
            // Remove from HashMap using the key stored in the LRU node
            cache.remove(lruNode.key);
            
            // Remove from Doubly-Linked List
            removeNode(lruNode);
        }

        // 3. Add New Entry
        Node newNode = new Node(key, value);
        
        // Add to HashMap and to the front of the list (MRU)
        cache.put(key, newNode);
        addFront(newNode);
    }
}