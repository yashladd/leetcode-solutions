class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        vowels = set("aeiou")
        
        # Iterate over every possible starting position
        for i in range(len(word)):
            current_vowels = set()
            # Expand to the right
            for j in range(i, len(word)):
                # If we hit a consonant, this substring and any extension of it are invalid
                if word[j] not in vowels:
                    break
                
                current_vowels.add(word[j])
                
                # If we have all 5 vowels, this is a valid vowel substring
                if len(current_vowels) == 5:
                    cnt += 1
                    
        return cnt