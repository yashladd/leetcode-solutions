class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        h = {}
        for i, ch in enumerate(order):
            h[ch] = i

        prev = words[0]
        for word in words[1:]:
            if word == prev:
                continue
            n1, n2 = len(prev), len(word)
            for j in range(n1):
                if j == n2:
                    return False
                if prev[j] != word[j]:
                    if h[prev[j]] > h[word[j]]:
                        return False
                    break
            prev = word
            
        return True