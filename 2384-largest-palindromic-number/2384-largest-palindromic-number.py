class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter
        
        # 1. Count frequencies of each digit
        counts = Counter(num)
        
        left_half = []
        
        # 2. Build the left half greedily from '9' down to '1'
        for d in "987654321":
            if counts[d] >= 2:
                pairs = counts[d] // 2
                left_half.append(d * pairs)
                counts[d] %= 2 # Keep track of the remainder
                
        # Handle '0's for the left half
        # Only add '0's if the left_half is NOT empty (no leading zeroes)
        if left_half and counts['0'] >= 2:
            pairs = counts['0'] // 2
            left_half.append('0' * pairs)
            counts['0'] %= 2
            
        left_str = "".join(left_half)
        
        # 3. Find the largest single middle digit
        middle = ""
        for d in "9876543210":
            if counts[d] > 0:
                middle = d
                break
                
        # 4. Assemble the final palindrome
        # If there's no left half and no middle, it means we only had zeroes
        if not left_str and not middle:
            return "0"
            
        return left_str + middle + left_str[::-1]