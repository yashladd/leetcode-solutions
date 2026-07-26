class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_longest_prefix(self) -> str:
        node = self.root
        prefix = []
        
        # We only continue down the Trie if:
        # 1. There is exactly one path down (meaning all words share this character)
        # 2. We haven't reached the end of any of the inserted words
        while len(node.children) == 1 and not node.is_end_of_word:
            # Get the only key-value pair in the dictionary
            char, next_node = list(node.children.items())[0]
            prefix.append(char)
            node = next_node
            
        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle edge cases where the list is empty or contains an empty string
        if not strs or "" in strs:
            return ""
            
        trie = Trie()
        
        # Insert all words into the Trie
        for word in strs:
            trie.insert(word)
            
        # Extract the common prefix
        return trie.get_longest_prefix()