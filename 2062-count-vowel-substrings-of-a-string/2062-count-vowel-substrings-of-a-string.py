class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        last_seen = {v: -1 for v in "aeiou"}
        start = 0
        ans = 0
        vowels = set("aeiou")
        
        for i, char in enumerate(word):
            if char not in vowels:
                # Reset window on consonant
                start = i + 1
                last_seen = {v: -1 for v in "aeiou"}
            else:
                last_seen[char] = i
                # If we have seen all 5 vowels in the current valid run
                if min(last_seen.values()) >= start:
                    # Valid substrings ending here start anywhere from 'start' 
                    # up to the earliest position of a required vowel.
                    ans += min(last_seen.values()) - start + 1
                    
        return ans