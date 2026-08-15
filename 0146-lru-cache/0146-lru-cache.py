from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    next: 'Node' = None
    prev: 'Node' = None

class EvictionPolicy(ABC):
    @abstractmethod
    def key_accessed(self, key: int, node: Node) -> None:
        """Called whenever an existing key is read or updated."""
        pass

    @abstractmethod
    def add_new(self, node: Node) -> None:
        """Called whenever a brand new key is added to the cache."""
        pass

    @abstractmethod
    def evict(self) -> Node:
        """Removes and returns the node that should be evicted."""
        pass

class LRUPolicy(EvictionPolicy):
    def __init__(self):
        # Using dummy nodes: MRU items near head, LRU items near tail
        self._head = Node(-1, -1)
        self._tail = Node(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _add_front(self, node: Node) -> None:
        """Helper to insert right after the dummy head (MRU side)."""
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def _delete_node(self, node: Node) -> None:
        """Helper to detach a node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def key_accessed(self, key: int, node: Node) -> None:
        # For LRU, we don't need the key, but we satisfy the interface
        self._delete_node(node)
        self._add_front(node)

    def add_new(self, node: Node) -> None:
        self._add_front(node)

    def evict(self) -> Node:
        # The LRU item is right before the dummy tail
        lru_node = self._tail.prev
        self._delete_node(lru_node)
        return lru_node

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._store: dict[int, Node] = {}
        # Inject the LRU Strategy into the generic cache
        self._policy: EvictionPolicy = LRUPolicy()

    def get(self, key: int) -> int:
        node = self._store.get(key)
        if node:
            # Delegate ordering logic to policy
            self._policy.key_accessed(key, node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self._store.get(key)
        if node:
            # Update value and notify policy
            node.val = value
            self._policy.key_accessed(key, node)
        else:
            # Capacity check
            if len(self._store) == self._capacity:
                evicted_node = self._policy.evict()
                del self._store[evicted_node.key]
            
            # Add new item
            new_node = Node(key, value)
            self._store[key] = new_node
            self._policy.add_new(new_node)