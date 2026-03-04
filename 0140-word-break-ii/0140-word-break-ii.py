class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        cache = {}

        def f(idx):
            if idx == len(s):
                return [""]

            res = []                
            curr = trie.root

            for j in range(idx, len(s)):
                ch = s[j]
                if ch not in curr.children:
                    break

                curr = curr.children[ch]
                if curr.isWord:
                    for suff in f(j+1):
                        if len(suff):
                            res.append(s[idx:j+1] + " " + suff)
                        else:
                            res.append(s[idx:j+1])
            
            return res

        return f(0)
