class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = None
        node.prev = None


    def addFront(self, node):
        secondLast = self.tail.prev
        secondLast.next = node
        node.prev = secondLast
        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.deleteNode(node)
        self.addFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.addFront(node)
        else:
            if len(self.cache) == self.capacity:
                leastRecentlyUsed = self.head.next
                self.deleteNode(leastRecentlyUsed)
                del self.cache[leastRecentlyUsed.key]

            mostRecentlyUsed = Node(key, value)
            self.cache[key] = mostRecentlyUsed
            self.addFront(mostRecentlyUsed)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)