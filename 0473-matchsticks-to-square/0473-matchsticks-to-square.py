class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        N = len(matchsticks)

        matchsticks.sort(reverse=True)

        summ = sum(matchsticks)

        if summ % 4:
            return False 

        side_len = summ // 4
        @cache
        def back(i, mask, matches, curr_side):

            if curr_side == side_len:
                return back(0, mask, matches + 1, 0)

            if matches == 3:
                return True

            if i == N:
                return False

            for j in range(N):

                if not (mask >> j & 1) and curr_side + matchsticks[j] <= side_len:
                    if back(j+1, mask | (1 << j), matches, curr_side + matchsticks[j]):
                        return True

            return False


        return back(0, 0, 0, 0)




