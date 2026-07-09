class Solution:
    def maximumSwap(self, num: int) -> int:

        maxi = num

        num_str = str(num)

        N = len(num_str)

        chars = list(num_str)


        for i in range(N):
            for j in range(N):
                if i != j:
                    chars[i], chars[j] = chars[j], chars[i]
                    maxi = max(maxi, int("".join(chars)))
                    chars[i], chars[j] = chars[j], chars[i]

        return maxi


        