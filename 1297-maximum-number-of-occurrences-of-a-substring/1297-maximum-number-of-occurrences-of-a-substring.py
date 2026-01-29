from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        counts = Counter()
        
        # Only iterate once with a fixed window of minSize
        for i in range(n - minSize + 1):
            sub = s[i : i + minSize]
            
            # Check the unique character constraint
            if len(set(sub)) <= maxLetters:
                counts[sub] += 1
                
        return max(counts.values(), default=0)