class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        char_indices = defaultdict(list)
        for idx, char in enumerate(text):
            char_indices[char].append(idx)
        
        if len(char_indices) == 1:
            return len(text)
        
        max_length = 0
        for char, indices in char_indices.items():
            total_occurrences = len(indices)
            left = 0  
            for right in range(total_occurrences):
                while indices[right] - indices[left] - (right - left) > 1:
                    left += 1

                current_window = right - left + 1
                if current_window < total_occurrences:
                    current_window += 1
                max_length = max(max_length, current_window)
        
        return max_length
        