class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]        
            return cur.isEnd
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)