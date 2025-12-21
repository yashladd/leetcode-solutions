class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 1. Quick lookup (O(1))
        wordSet = set(wordDict)
        
        # 2. Memoization Cache
        memo = {}

        def rec(i):
            # If we already computed this index, return the saved list of sentences
            if i in memo:
                return memo[i]
            
            # Base Case: Reached end of string. 
            # Return a list with empty string to indicate a valid path was found.
            if i == len(s):
                return [""]
            
            results = []
            
            # Loop to find valid words starting at 'i'
            for j in range(i, len(s)):
                current_word = s[i : j+1]
                
                # *** FIX: Replace 'is_valid_word' with actual check ***
                if current_word in wordSet:
                    
                    # RECURSIVE STEP: Get all valid suffixes (sentence endings)
                    suffixes = rec(j + 1)
                    
                    # COMBINE: Join current_word with every valid suffix
                    for suffix in suffixes:
                        if suffix == "":
                            # We reached the end, so just add the word itself
                            results.append(current_word)
                        else:
                            # We have more words, so add a space
                            results.append(current_word + " " + suffix)
            
            # Cache the result for index 'i'
            memo[i] = results
            return results

        return rec(0)