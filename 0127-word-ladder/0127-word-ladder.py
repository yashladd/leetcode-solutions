class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque([(beginWord, 1)])
        chrs = "abcdefghijklmnopqrstuvwxyz"
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in chrs:
                    trans = word[:i] + ch + word[i+1:]
                    if trans in words:
                        q.append((trans, steps + 1))
                        words.discard(trans)
                
        return 0
        
        