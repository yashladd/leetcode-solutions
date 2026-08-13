from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        vocab = set(wordDict)
        
        @cache
        def dfs(i):
            # Base case: reached the end of the string
            if i == len(s):
                return [""]
            
            valid_sentences = []
            
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in vocab:
                    # Recursively get all valid sentence endings from index j
                    for tail in dfs(j):
                        if tail:
                            valid_sentences.append(word + " " + tail)
                        else:
                            # If tail is empty string (we are at the end)
                            valid_sentences.append(word)
                            
            return valid_sentences
            
        return dfs(0)