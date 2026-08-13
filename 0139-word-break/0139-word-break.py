class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        can_break = [False] * (N+1)
        can_break[N] = True
        vocab = set(wordDict)

        for end_idx in range(N-1, -1, -1):
            for start_idx in range(end_idx+1):
                word = s[start_idx: end_idx+1]
                if word in vocab:
                    if can_break[end_idx+1]:
                        can_break[start_idx] = True

        return can_break[0]
