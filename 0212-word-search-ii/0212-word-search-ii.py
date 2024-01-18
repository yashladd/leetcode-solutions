class Node:
    def __init__(self):
        self. children  = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isWord = True
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)
            
        r, c = len(board), len(board[0])
        def inb(p, q):
            return p < r and p >= 0 and q < c and q >= 0
        
        vis = [[0] * c for _ in range(r)]  
        def dfs(i, j, node, path, vis):
            if not inb(i,j) or board[i][j] not in node.children or vis[i][j]: return 
            path += board[i][j]
            # print("IJ",i, j, path, node.isWord,node.children.keys())
            vis[i][j] = 1
            node = node.children[board[i][j]]
            if node.isWord:
                # print("reached")
                res.add(path)
                # return 
            
            
            # print(node.children.keys())
            dfs(i + 1, j, node, path, vis)
            dfs(i, j + 1, node, path, vis)
            dfs(i - 1, j, node, path, vis)
            dfs(i, j-1, node, path, vis)
            
        
            vis[i][j] = 0
            
        res = set()
        root = trie.root
        for i in range(r):
            for j in range(c):
                dfs(i, j, root, "", vis)
        
        return list(res)
            
        
        