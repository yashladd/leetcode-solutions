from dataclasses import dataclass
@dataclass
class Node:
    key: int
    val: int
    next: Optional[Node] = None
    prev: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._head = Node(-1, -1)
        self._tail = Node(-1,-1)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
        self._cache = {}

    def _move_to_end(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        tail_prev = self._tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self._tail
        self._tail.prev = node
        

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._move_to_end(node)
        return node.val

    def _evict_front(self):
        node = self._head.next
        self._head.next = self._head.next.next
        self._head.next.prev = self._head
        node.next = None
        node.prev = None
        return node
        
    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._move_to_end(node)
            return 

        if len(self._cache) == self._capacity:
            node = self._evict_front()

            del self._cache[node.key]

        node_to_insert = Node(key, value)
        
        self._tail.prev.next = node_to_insert
        node_to_insert.prev = self._tail.prev
        node_to_insert.next = self._tail
        self._tail.prev = node_to_insert

        self._cache[key] = node_to_insert

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)