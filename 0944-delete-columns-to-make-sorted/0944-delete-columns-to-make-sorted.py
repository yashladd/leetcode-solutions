class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        
        # zip(*strs) is an iterator! 
        # It yields one column at a time ('c', 'd', 'g') without building the whole grid.
        for col in zip(*strs):
            # Check if this column is sorted
            # We iterate through the column tuple to find any unsorted pair
            for i in range(len(col) - 1):
                if col[i] > col[i+1]:
                    delete_count += 1
                    break # Safe to break here because 'col' is already fully consumed by zip
                    
        return delete_count