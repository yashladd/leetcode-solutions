class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wl = set(wordList)
        q = deque([(beginWord, 1)])
        see = set()
        see.add(beginWord)
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for i in range(len(w)):
                for ch in list(map(chr, range(ord('a'), ord('a') + 26))):
                    t = w[:i] + ch + w[i+1:] 
                    if t in wl and t not in see:
                        q.append((t, d + 1))
                        see.add(t)
        
        return 0
            