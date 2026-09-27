class Node:
    def __init__(self, isEnd = False):
        self.chars = {}
        self.word = None
        
        
class Trie:
    def __init__(self, dictonary = set()):
        self.root = Node()
        for w in dictonary:
            curr = self.root
            for ch in w:
                if ch not in curr.chars:
                    curr.chars[ch] = Node()
                curr = curr.chars[ch]
            curr.word = w
            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie(set(words))
        n, m = len(board), len(board[0])
        res = []
        root = t.root
        
        def find(i, j, node):
            if i < 0 or j < 0 or i >= n or j >=m:
                return 
            
            if board[i][j] == "#":
                return 
            
            
            char = board[i][j]
            
            if char not in node.chars:
                return 
            
            
            board[i][j] = "#"
            node = node.chars[char]
            if node.word is not None:
                # res.append("".join(curr[:]))
                res.append(node.word)
                node.word = None
                
            find(i+1, j, node)
            find(i-1, j, node)
            find(i, j+1, node)
            find(i, j-1, node)
            
            board[i][j] = char
            
        for i in range(n):
            for j in range(m):
                # vis = [[0 for _ in range(m)] for _ in range(n)] 
                find(i, j, root)
                
        return res
        
        
    
            
            
            
            
        
        
        