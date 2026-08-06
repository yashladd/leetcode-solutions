class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        N = len(arr)
        res = []

        for window_size in range(N, 1,-1):
            curr_window = arr[:window_size]
            max_val = max(curr_window)
            # Note the arr elements are unique
            idx = curr_window.index(max_val)

            if idx == len(curr_window) - 1:
                continue

            if idx != 0:
                res.append(idx+1)

                arr[:idx+1] = arr[:idx+1][::-1]

            res.append(window_size)

            arr[:window_size] = arr[:window_size][::-1]


        return res