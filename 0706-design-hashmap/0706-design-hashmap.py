class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.capacity = 1000 # Start smaller to demonstrate resizing
        self.size = 0
        self.load_factor = 0.75
        self.table = [Node(-1, -1) for _ in range(self.capacity)]

    def _hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        curr = self.table[idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        
        # New key insertion
        curr.next = Node(key, value)
        self.size += 1
        
        # Check if we need to resize
        if self.size / self.capacity >= self.load_factor:
            self._resize()

    def _resize(self):
        old_table = self.table
        self.capacity *= 2  # Double the capacity
        self.size = 0       # Reset size, it will be re-counted during put
        self.table = [Node(-1, -1) for _ in range(self.capacity)]
        
        # Rehash all existing elements
        for head in old_table:
            curr = head.next
            while curr:
                # We reuse the put logic to insert into the new table
                self.put(curr.key, curr.val)
                curr = curr.next

    def get(self, key: int) -> int:
        idx = self._hash(key)
        curr = self.table[idx].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        curr = self.table[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next