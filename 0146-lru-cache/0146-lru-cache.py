from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    next: Node | None = None
    prev: Node | None = None

class LinkedList:
    def __init__(self):
        self._tail = Node(-1, -1)
        self._head = Node(-1, -1)
        self._tail.next = self._head
        self._head.prev= self._tail

    def add_front(self, node):
        self._head.prev.next = node
        node.prev = self._head.prev

        node.next = self._head
        self._head.prev = node

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev= None
        node.next = None

    def remove_last(self):
        lru_node = self._tail.next
        self._tail.next = lru_node.next
        lru_node.next.prev = self._tail

        lru_node.next = None
        lru_node.prev = None

        return lru_node


class LRUCache:

    def __init__(self, capacity: int):
        self._cap: int = capacity
        self._store: dict[int, Node] = {}
        self._ordering: LinkedList = LinkedList()

    def _key_accessed(self, key, node):
        self._ordering.delete_node(node)
        self._ordering.add_front(node)

    def _evict(self):
        return self._ordering.remove_last()
        

    def get(self, key: int) -> int:
        node = self._store.get(key)
        if node is not None:
            self._key_accessed(key, node)
            return self._store[key].val;
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self._store.get(key)
        if node is not None:
            node.val = value
            self._key_accessed(key, node)
        else:
            if len(self._store) == self._cap:
                lru_node = self._evict()
                del self._store[lru_node.key]


            node = Node(key, value)
            self._store[key] = node
            self._ordering.add_front(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)