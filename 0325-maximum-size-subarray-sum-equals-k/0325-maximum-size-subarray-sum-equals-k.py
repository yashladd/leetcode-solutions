class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        max_len = 0
        # Map prefix_sum to its FIRST index.
        # Initialize with {0: -1} to handle subarrays starting from the beginning.
        indices = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            # Check if there is a previous prefix sum such that:
            # curr_sum - old_sum = k  =>  old_sum = curr_sum - k
            if prefix_sum - k in indices:
                length = i - indices[prefix_sum - k]
                max_len = max(max_len, length)

            # Only add the prefix_sum if it's not already in the map.
            # We want to keep the earliest index to maximize length.
            if prefix_sum not in indices:
                indices[prefix_sum] = i

        return max_len