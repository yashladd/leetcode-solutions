from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Iterate through every character index in the word
        for i in range(len(word)):
            # Create a version of the word with the i-th character removed
            temp_word = word[:i] + word[i+1:]
            
            # Count frequencies of the new truncated word
            counts = Counter(temp_word).values()
            
            # If all counts are the same (set length is 1), we found a solution
            if len(set(counts)) == 1:
                return True
                
        return False