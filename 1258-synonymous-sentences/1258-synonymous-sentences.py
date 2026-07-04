from collections import defaultdict
from typing import List

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = {}
        
        # 1. Union-Find: Find operation with path compression
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 2. Union-Find: Union operation to connect synonyms
        for u, v in synonyms:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                
        # 3. Group all connected synonyms by their absolute root
        groups = defaultdict(list)
        for word in parent:
            root = find(word)
            groups[root].append(word)
            
        # Sort each group lexicographically so our output is naturally sorted
        for root in groups:
            groups[root].sort()
            
        # 4. Backtrack to build the sentences
        words = text.split()
        res = []
        
        def backtrack(index, current_sentence):
            # Base case: sentence is fully built
            if index == len(words):
                res.append(" ".join(current_sentence))
                return
            
            word = words[index]
            
            # If the word is in our Union-Find structure, branch out for all its synonyms
            if word in parent:
                root = find(word)
                for syn in groups[root]:
                    current_sentence.append(syn)
                    backtrack(index + 1, current_sentence)
                    current_sentence.pop()
            # Otherwise, just keep the word and move forward
            else:
                current_sentence.append(word)
                backtrack(index + 1, current_sentence)
                current_sentence.pop()
                
        backtrack(0, [])
        return res