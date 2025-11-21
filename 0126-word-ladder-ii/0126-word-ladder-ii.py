from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wl = set(wordList)
        if endWord not in wl:
            return []
        
        # 1. BFS to build the 'parents' graph
        # 'layer' contains the current set of words we are visiting
        layer = {beginWord}
        parents = defaultdict(set)
        
        # We remove words from wl only after processing the whole level
        wl.discard(beginWord)
        
        found = False
        
        while layer and not found:
            next_layer = set()
            words_to_remove = set()
            
            for w in layer:
                for i in range(len(w)):
                    # Try changing each character to a-z
                    for char_code in range(97, 123):
                        ch = chr(char_code)
                        if ch == w[i]:
                            continue
                            
                        t = w[:i] + ch + w[i+1:]
                        
                        if t in wl:
                            # We found a valid next word
                            next_layer.add(t)
                            parents[t].add(w) # Record the parent to reconstruct path later
                            words_to_remove.add(t)
                            
                            if t == endWord:
                                found = True
            
            # Remove visited words from the main set so we don't visit them again
            # (This ensures we only find shortest paths)
            wl -= words_to_remove
            layer = next_layer
        
        if not found:
            return []
            
        # 2. DFS (Backtracking) to reconstruct paths from endWord -> beginWord
        res = []
        def backtrack(node, path):
            if node == beginWord:
                # We reached the start, add the full reversed path to results
                res.append([beginWord] + path[::-1])
                return
            
            # Go through all recorded parents
            if node in parents:
                for p in parents[node]:
                    backtrack(p, path + [node])
        
        backtrack(endWord, [])
        return res