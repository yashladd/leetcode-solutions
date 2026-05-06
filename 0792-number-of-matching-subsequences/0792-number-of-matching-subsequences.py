class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_map = defaultdict(list)

        for w in words:
            it = iter(w)
            char_map[next(it)].append(it)
        ans = 0
        for ch in s:
            curr_match_chars = char_map[ch]
            char_map[ch] = []
            for prevIt in curr_match_chars:
                nex = next(prevIt, None)
                if not nex:
                    ans += 1
                    continue
                char_map[nex].append(prevIt)

        return ans 