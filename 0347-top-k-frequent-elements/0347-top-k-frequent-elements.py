import random
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build a hash map of element frequencies
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_frequency = count[unique[pivot_index]]
            
            # Move pivot to the end temporarily
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            store_index = left
            # Move all elements with a higher frequency to the left
            for i in range(left, right):
                if count[unique[i]] > pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            # Move the pivot back to its final, correct position
            unique[right], unique[store_index] = unique[store_index], unique[right]
            
            return store_index
            
        def quickselect(left: int, right: int, k_target: int) -> None:
            if left >= right:
                return
            
            # Pick a random pivot to ensure O(N) average time complexity
            pivot_index = random.randint(left, right)
            
            # Partition the array and get the pivot's final position
            pivot_index = partition(left, right, pivot_index)
            
            # If the pivot is exactly at the k-th position, we're done
            if pivot_index == k_target:
                return
            # If the pivot is greater than k, the top k elements are to the left
            elif pivot_index > k_target:
                quickselect(left, pivot_index - 1, k_target)
            # If the pivot is less than k, we need to include elements to the right
            else:
                quickselect(pivot_index + 1, right, k_target)

        # 2. Run quickselect to partition the first k elements
        n = len(unique)
        quickselect(0, n - 1, k)
        
        # 3. The first k elements of the unique array are now the most frequent
        return unique[:k]