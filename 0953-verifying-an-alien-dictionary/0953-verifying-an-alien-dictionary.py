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
            i, j = 0, 0
            matched = 0
            while i < n1 and j < n2 and prev[i] == word[j]:
                i += 1
                j += 1
            
            if i == n1 or j == n2:
                if n1 > n2 and j == n2:
                    return False
                else:
                    prev = word
                    continue
            if h[prev[i]] > h[word[j]]:
                    return False
            
            prev = word
            
        return True