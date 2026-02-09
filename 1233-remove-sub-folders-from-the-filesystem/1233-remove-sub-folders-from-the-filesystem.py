class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        
        # 1. Build Trie (O(N * L))
        for path in folder:
            node = root
            for part in path.split('/')[1:]:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]
            node.is_end = True
        
        res = []
        
        # 2. Check each path against Trie (O(N * L))
        for path in folder:
            node = root
            parts = path.split('/')[1:]
            is_sub = False
            
            for i, part in enumerate(parts):
                node = node.children[part]
                # If we hit a node that is an end, AND it's not the node 
                # for the current path itself (meaning it's a prefix),
                # then 'path' is a sub-folder.
                if node.is_end and i < len(parts) - 1:
                    is_sub = True
                    break
            
            if not is_sub:
                res.append(path)
                
        return res