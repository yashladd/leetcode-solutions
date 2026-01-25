class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        [3 8 1 2 9 5 7] k = 3
        [1 2 3 5 7 8 9]
         0 1 2 3 4 5 6
        1 1 2 3 4 4 4 4 5
        n = 7
        """
        mini = float("inf")
        h = Counter(nums)
        sortedNumsWithCnt = list(sorted(h.items()))
        print(sortedNumsWithCnt)
        n = len(sortedNumsWithCnt)
        for i, (num, cnt) in enumerate(sortedNumsWithCnt):
            # if i >= len(sortedNumsWithCnt)-1:
            #     con
            print(i, num, cnt)
            if cnt >= k:
                mini = 0
            else:
                nextBig = float("inf")
                remaining = k - cnt
                # print(i , num , cnt, nextBig, remaining)
                while remaining > 0 and i + 1 < n:
                    remaining -= sortedNumsWithCnt[i+1][1]
                    nextBig = sortedNumsWithCnt[i+1][0]
                    i += 1
                # print(i , num , cnt, nextBig, remaining)
                if remaining <= 0:
                    mini = min(mini, nextBig - num)

        
    
        return mini

        