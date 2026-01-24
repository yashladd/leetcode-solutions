class Solution:
    def getColumnState(self, curr, i, m):
        # print(curr, i)
        if i == m:
            self.validStates.append(curr[:])
            return 

        for ch in ["R", "G", "B"]:
            if (not curr) or ch != curr[-1]:
                self.getColumnState(curr + ch, i+1, m)

    @cache
    def solve(self, prevInd, remStates):
        if remStates == 0:
            return 1

        ways = 0
        prevState = self.validStates[prevInd]
        for i in range(len(self.validStates)):
            if i != prevInd:
                currState = self.validStates[i]

                isValid = True

                for c1, c2 in zip(prevState, currState):
                    if c1 == c2:
                        isValid = False
                        break

                if isValid:
                    ways = (ways + self.solve(i, remStates -1)) % self.MOD
        return ways

                

    def colorTheGrid(self, m: int, n: int) -> int:
        self.validStates = []
        self.MOD = 10**9 + 7
        self.getColumnState("", 0, m)

        ways = 0

        for i in range(len(self.validStates)):
            ways = (ways + self.solve(i, n-1)) % self.MOD

        return ways
        