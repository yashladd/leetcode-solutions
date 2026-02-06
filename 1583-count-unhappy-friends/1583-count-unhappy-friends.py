class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        for u, v pair
        
        dict (v: u + v:u)

        """

        paired = {}
        for u, v in pairs:
            paired[u] = v
            paired[v] = u

        rank = defaultdict(lambda: {})

        for person1, pref in enumerate(preferences):
            for wt, person2 in enumerate(pref):
                rank[person1][person2] = wt

        cnt = 0
        for x in range(n):
            y = paired[x]
            isUnhappy = False
            for u in preferences[x]:
                if u == y:
                    break

                v = paired[u]

                if rank[u][x] < rank[u][v]:
                    isUnhappy = True
                    break

            if isUnhappy:
                cnt += 1

        return cnt

