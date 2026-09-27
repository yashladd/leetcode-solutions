class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        N = len(matchsticks)

        matchsticks.sort(reverse=True)

        summ = sum(matchsticks)

        if summ % 4:
            return False 

        side_len = summ // 4
        @cache
        def back(mask, matches, curr_side):

            if curr_side == side_len:
                return back(mask, matches + 1, 0)

            if matches == 3:
                return True


            for j in range(N):

                if not (mask >> j & 1) and curr_side + matchsticks[j] <= side_len:
                    if back(mask | (1 << j), matches, curr_side + matchsticks[j]):
                        return True

            return False


        return back(0, 0, 0)




