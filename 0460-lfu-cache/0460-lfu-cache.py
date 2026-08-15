from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Node:
    key: int
    val: int
    freq: int
    next: Node | None = None
    prev: Node | None = None

class DLL:
    def __init__(self):
        self.tail = Node(-1, -1, -1)
        self.head = Node(-1, -1, -1)
        self.tail.next = self.head
        self.head.prev = self.tail
        self.size = 0

    def add_front(self, node):
        self.head.prev.next = node
        node.prev = self.head.prev

        node.next = self.head
        self.head.prev = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
        self.size -= 1

    def remove_last(self) -> Node:
        if self.size == 0:
            return 

        last_node = self.tail.next
        self.remove_node(last_node)
        return last_node


class EvictionPolicy(ABC):

    @abstractmethod
    def insert(self, node):
        pass

    @abstractmethod
    def touch(self, node) -> None:
        pass


    @abstractmethod
    def evict(self) -> Node:
        pass


class LFUPolicy(EvictionPolicy):

    def __init__(self):
        self._ordering_at = defaultdict(DLL)
        self._min_freq = 0


    def insert(self, node):
        self._min_freq = 1
        node.freq = 1
        self._ordering_at[1].add_front(node)



    def touch(self, node) -> None:
        prev_freq = node.freq
        dll = self._ordering_at[prev_freq]
        dll.remove_node(node)

        node.freq += 1
        if dll.size == 0:
            del self._ordering_at[prev_freq] 
            if self._min_freq == prev_freq:
                self._min_freq += 1

        self._ordering_at[node.freq].add_front(node)


    def evict(self) -> Node:
        dll = self._ordering_at[self._min_freq]
        evicted = dll.remove_last()
        freq = evicted.freq

        if dll.size == 0:
            del self._ordering_at[evicted.freq]

            # while freq + 1 not in self._ordering_at or self._ordering_at[freq + 1].size == 0:
            #     freq += 1
            # self._min_freq = freq

        return evicted

class GenericCache:

    def __init__(self, capacity: int, policy: EvictionPolicy):
        self._policy = policy
        self._cap = capacity
        self._store: dict[int, Node] = {}
        

    def get(self, key: int) -> int:
        if key not in self._store:
            return -1

        node = self._store[key]
        self._policy.touch(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self._store:
            node = self._store[key]
            node.val = value
            self._policy.touch(node)
        else:
            if len(self._store) == self._cap:
                evicted = self._policy.evict()
                del self._store[evicted.key]

            node = Node(key, value, 1)
            self._store[key] = node
            self._policy.insert(node)

class LFUCache(GenericCache):

    def __init__(self, capacity: int):
        super().__init__(capacity, LFUPolicy())
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)