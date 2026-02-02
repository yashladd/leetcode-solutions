class Node:
    def __init__(self, isEnd = False):
        self.chars = {}
        self.isEnd = isEnd
        
        
class Trie:
    def __init__(self, dictonary = set()):
        self.root = Node()
        for w in dictonary:
            curr = self.root
            for ch in w:
                if ch not in curr.chars:
                    curr.chars[ch] = Node()
                curr = curr.chars[ch]
            curr.isEnd = True
            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(set(words))
        n, m = len(board), len(board[0])
        res = []
        root = t.root
        
        def find(i, j, node, vis, curr):
            if i < 0 or j < 0 or i >= n or j >=m:
                return 
            
            if vis[i][j]: return 
            
            
            char = board[i][j]
            
            if char not in node.chars:
                return 
            
            
            vis[i][j]  = 1
            node = node.chars[char]
            if node.isEnd:
                # res.append("".join(curr[:]))
                res.append("".join(curr + [char]))
                node.isEnd = False
                
            find(i+1, j, node, vis, curr + [char])
            find(i-1, j, node, vis, curr + [char])
            find(i, j+1, node, vis, curr + [char])
            find(i, j-1, node, vis, curr + [char])
            
            vis[i][j] = 0
            
        for i in range(n):
            for j in range(m):
                vis = [[0 for _ in range(m)] for _ in range(n)] 
                find(i, j, root, vis, [])
                
        return res
        
        
    
            
            
            
            
        
        
        