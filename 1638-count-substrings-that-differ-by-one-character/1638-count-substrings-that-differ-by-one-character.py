class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        n, m = len(s), len(t)
        
        # Iterate over every starting character in s
        for i in range(n):
            # Iterate over every starting character in t
            for j in range(m):
                diff = 0
                # Expand both substrings as long as we don't run out of bounds
                for k in range(min(n - i, m - j)):
                    # Compare characters at current offset k
                    if s[i + k] != t[j + k]:
                        diff += 1
                    
                    # If we have exactly 1 difference, this substring pair counts
                    if diff == 1:
                        ans += 1
                    # If we exceed 1 difference, this path is invalid; stop expanding
                    elif diff > 1:
                        break
                        
        return ans