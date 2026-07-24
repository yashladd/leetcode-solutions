class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_to_idx = {0:-1}

        curr_sum = 0
        best_subarray_len = 0
        for i, v in enumerate(nums):
            if v == 0:
                curr_sum -= 1
            elif v == 1:
                curr_sum += 1


            if curr_sum in sum_to_idx:
                best_subarray_len = max(best_subarray_len, i - sum_to_idx[curr_sum])
            else:
                sum_to_idx[curr_sum] = i

        return best_subarray_len

