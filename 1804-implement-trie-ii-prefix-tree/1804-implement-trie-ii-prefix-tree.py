class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # How many words start with or pass through this node
        self.end_count = 0     # How many words end exactly at this node

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.prefix_count += 1
        cur.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.prefix_count

    def erase(self, word: str) -> None:
        cur = self.root
        for ch in word:
            # We assume word exists per constraints, but safety check is fine
            if ch not in cur.children:
                return
            
            cur.children[ch].prefix_count -= 1
            next_node = cur.children[ch]
            
            # Optimization: Prune the tree if count is 0
            # (Note: You can skip this if strictly following simple logic, 
            # but it's good for memory)
            if next_node.prefix_count == 0:
                del cur.children[ch]
                return 
            
            cur = next_node
            
        cur.end_count -= 1