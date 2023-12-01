class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord)!= len(endWord): return 0
        bets = 'abcdefghijklmnopqrstuvwxyz'
        q = deque([beginWord])
        tr = 0
        words = set(wordList)
        words.discard(beginWord)
        while q:
            sz = len(q)
            tr += 1
            for _ in range(sz):
                curr = q.popleft()
                if curr == endWord:
                    return tr
                for idx in range(len(curr)):
                    for ch in bets:
                        match = curr[:idx] + ch + curr[idx+1:] 
                        # if match  == endWord:
                        #     return tr + 1
                        if match in words:
                            q.append(match)
                            words.discard(match)

                            
        return 0
                
        