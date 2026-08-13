class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        vocab = set(wordDict)
        cache = {}
        return self._can_break(0, s, vocab, cache)


    def _can_break(self, idx: int, s: str, vocab: set[str], cache: dict[int, bool]):
        if idx >= len(s):
            return True

        if idx in cache:
            return cache[idx]

        for break_idx in range(idx+1, len(s)+1):
            broken_word = s[idx: break_idx]
            if broken_word in vocab:
                is_success =  self._can_break(break_idx, s, vocab, cache)
                if is_success:
                    cache[idx] = True
                    return True
        cache[idx] = False
        return False



