from abc import ABC, abstractmethod
from collections import defaultdict

# ==========================================
# 1. Shared Data Structures
# ==========================================

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1  # Required for LFU
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """A standalone DLL used by both LRU and LFU policies."""
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def remove_last(self) -> Node:
        if self.size == 0:
            return None
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

# ==========================================
# 2. Abstract Policy Interface
# ==========================================

class EvictionPolicy(ABC):
    @abstractmethod
    def insert(self, node: Node) -> None:
        """Called when a brand new key is added."""
        pass

    @abstractmethod
    def touch(self, node: Node) -> None:
        """Called when an existing key is read or updated."""
        pass

    @abstractmethod
    def evict(self) -> Node:
        """Removes and returns the node that should be evicted."""
        pass

# ==========================================
# 3. Concrete Implementations
# ==========================================

class LRUPolicy(EvictionPolicy):
    def __init__(self):
        self.dll = DoublyLinkedList()

    def insert(self, node: Node) -> None:
        self.dll.add_front(node)

    def touch(self, node: Node) -> None:
        self.dll.remove_node(node)
        self.dll.add_front(node)

    def evict(self) -> Node:
        return self.dll.remove_last()

class LFUPolicy(EvictionPolicy):
    def __init__(self):
        self.freq_map = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def insert(self, node: Node) -> None:
        node.freq = 1
        self.min_freq = 1
        self.freq_map[1].add_front(node)

    def touch(self, node: Node) -> None:
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        # If we just removed the last node in the minimum frequency bucket, increment min_freq
        if self.freq_map[freq].size == 0 and self.min_freq == freq:
            self.min_freq += 1
            
        node.freq += 1
        self.freq_map[node.freq].add_front(node)

    def evict(self) -> Node:
        # Get the DLL for the lowest frequency and evict its LRU node
        return self.freq_map[self.min_freq].remove_last()

# ==========================================
# 4. Generic Cache Component
# ==========================================

class GenericCache:
    """The core engine that handles storage and capacity, delegating ordering to the policy."""
    def __init__(self, capacity: int, policy: EvictionPolicy):
        self._capacity = capacity
        self._store: dict[int, Node] = {}
        self._policy = policy

    def get(self, key: int) -> int:
        if key not in self._store:
            return -1
        
        node = self._store[key]
        self._policy.touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
            
        if key in self._store:
            node = self._store[key]
            node.val = value
            self._policy.touch(node)
        else:
            if len(self._store) == self._capacity:
                evicted_node = self._policy.evict()
                del self._store[evicted_node.key]
            
            new_node = Node(key, value)
            self._store[key] = new_node
            self._policy.insert(new_node)

# ==========================================
# 5. LeetCode Wrappers
# ==========================================

class LRUCache(GenericCache):
    def __init__(self, capacity: int):
        super().__init__(capacity, LRUPolicy())

