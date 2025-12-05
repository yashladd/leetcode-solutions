class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        # Iterate through the string to find top-level special substrings
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            # When count is 0, we found a balanced substring s[i:j+1]
            if count == 0:
                # 1. Identify the inner part: s[i+1:j] (strip outer 1 and 0)
                # 2. Recurse on the inner part to maximize it
                # 3. Add the outer 1 and 0 back
                inner_maximized = self.makeLargestSpecial(s[i+1:j])
                res.append('1' + inner_maximized + '0')
                
                # Move start pointer to the next character
                i = j + 1
        
        # Sort the processed substrings in descending order to get lexicographical max
        # Example: ['10', '1100'] becomes ['1100', '10']
        res.sort(reverse=True)
        
        return "".join(res)